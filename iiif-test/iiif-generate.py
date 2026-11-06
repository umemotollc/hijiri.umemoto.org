
from PIL import Image
import json
import glob
import os
import shutil
from urllib.parse import quote

BASE = "https://hijiri.umemoto.org/iiif-test"

BOOK = "MATSUMURA-Sotojiro-Passport-1931"

# 元画像
files = sorted(
    glob.glob("sotojiro-passport/*.jpeg")
)

if not files:
    raise RuntimeError("JPEG画像が見つかりません。")

# 出力先
image_root = f"images/{BOOK}"
thumbnail_root = f"thumbnails/{BOOK}"

os.makedirs(image_root, exist_ok=True)
os.makedirs(thumbnail_root, exist_ok=True)
os.makedirs("manifests", exist_ok=True)

# Manifest
manifest = {
    "@context": "http://iiif.io/api/presentation/3/context.json",
    "id": f"{BASE}/manifests/{BOOK}.json",
    "type": "Manifest",
    "label": {
        "ja": ["松村外次郎 パスポート 1931年 日本, 砺波市美術館"],
        "en": ["MATSUMURA Sotojiro Passport 1931, Japan, Tonami Museum of Art"]
    },
    "viewingDirection": "left-to-right",
    "behavior": ["paged"],
    "items": [],
    "metadata": [
        {
            "label": {"ja": ["資料種別"]},
            "value": {"ja": ["パスポート"]}
        },
        {
            "label": {"ja": ["発行国"]},
            "value": {"ja": ["日本"]}
        },
        {
            "label": {"ja": ["発行機関"]},
            "value": {"ja": ["外務省"]}
        }
    ]
}

for i, filepath in enumerate(files, 1):

    # 元のファイル名
    filename = os.path.basename(filepath)

    # 元画像を出力先へコピー
    output_path = os.path.join(image_root, filename)
    shutil.copy2(filepath, output_path)

    # 元画像URL
    image_url = (
        f"{BASE}/images/{BOOK}/{quote(filename)}"
    )

    # 画像を読み込み
    with Image.open(filepath) as img:

        # 元画像の寸法
        width, height = img.size

        # サムネイル生成（長辺500px）
        thumb = img.copy()
        thumb.thumbnail(
            (500, 500),
            Image.Resampling.LANCZOS
        )

        # サムネイル保存
        thumbnail_path = os.path.join(
            thumbnail_root,
            filename
        )

        thumb.convert("RGB").save(
            thumbnail_path,
            "JPEG",
            quality=85,
            optimize=True
        )

        # サムネイルの寸法
        thumb_width, thumb_height = thumb.size

    # サムネイルURL
    thumbnail_url = (
        f"{BASE}/thumbnails/{BOOK}/{quote(filename)}"
    )

    # Presentation API Canvas
    canvas_id = (
        f"{BASE}/manifests/{BOOK}/canvas/p{i}"
    )

    canvas = {
        "id": canvas_id,
        "type": "Canvas",
        "label": {
            "ja": [f"{i}フレーム"]
        },
        "width": width,
        "height": height,

        # サムネイル
        "thumbnail": [{
            "id": thumbnail_url,
            "type": "Image",
            "format": "image/jpeg",
            "width": thumb_width,
            "height": thumb_height
        }],

        "items": [{
            "id": f"{canvas_id}/page",
            "type": "AnnotationPage",

            "items": [{
                "id": f"{canvas_id}/annotation",
                "type": "Annotation",
                "motivation": "painting",

                # 元画像を直接参照
                "body": {
                    "id": image_url,
                    "type": "Image",
                    "format": "image/jpeg",
                    "width": width,
                    "height": height
                },

                "target": canvas_id
            }]
        }]
    }

    manifest["items"].append(canvas)

    print(
        f"Generated {i}/{len(files)}: {filename}"
    )


# Manifestを書き出す
manifest_path = f"manifests/{BOOK}.json"

with open(
    manifest_path,
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        manifest,
        f,
        ensure_ascii=False,
        indent=2
    )

print()
print(f"Manifest generated: {manifest_path}")
print(f"Total images: {len(files)}")
print(f"Total thumbnails: {len(files)}")
