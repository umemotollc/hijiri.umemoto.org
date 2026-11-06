from PIL import Image
import json
import glob
import os
import shutil

BASE = "https://hijiri.umemoto.org/iiif-test"

BOOK = "MATSUMURA-Sotojiro-Passport-1931"

# 元画像
files = sorted(
    glob.glob("sotojiro-passport/*.jpeg")
)

if not files:
    raise RuntimeError("JPEG画像が見つかりません。")

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

# 出力先
image_root = f"images/{BOOK}"

os.makedirs(image_root, exist_ok=True)
os.makedirs("manifests", exist_ok=True)


for i, filepath in enumerate(files, 1):

    filename = os.path.basename(filepath)

    # 元画像の寸法
    with Image.open(filepath) as img:
        width, height = img.size

    # IIIF Image APIのID
    image_id = f"{BASE}/images/{BOOK}/page{i:03d}"

    # ローカル出力ディレクトリ
    page_dir = f"{image_root}/page{i:03d}"

    os.makedirs(page_dir, exist_ok=True)

    # IIIF Image APIの静的画像ファイルを生成
    static_image_dir = f"{page_dir}/full/max/0"
    os.makedirs(static_image_dir, exist_ok=True)
    shutil.copyfile(
        filepath,
        f"{static_image_dir}/default.jpg"
    )

    # IIIF Image API info.json
    info = {
        "@context": "http://iiif.io/api/image/3/context.json",
        "id": image_id,
        "type": "ImageService3",
        "protocol": "http://iiif.io/api/image",
        "profile": "level0",
        "width": width,
        "height": height
    }

    with open(
        f"{page_dir}/info.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            info,
            f,
            ensure_ascii=False,
            indent=2
        )

    # Presentation API Canvas
    canvas_id = f"{BASE}/manifests/{BOOK}/canvas/p{i}"

    canvas = {
        "id": canvas_id,
        "type": "Canvas",
        "label": {
            "ja": [f"{i}フレーム"]
        },
        "width": width,
        "height": height,

        "items": [{
            "id": f"{canvas_id}/page",
            "type": "AnnotationPage",

            "items": [{
                "id": f"{canvas_id}/annotation",
                "type": "Annotation",
                "motivation": "painting",

                "body": {
                    "id": f"{image_id}/full/max/0/default.jpg",
                    "type": "Image",
                    "format": "image/jpeg",
                    "width": width,
                    "height": height,

                    "service": [{
                        "id": image_id,
                        "type": "ImageService3",
                        "profile": "level0"
                    }]
                },

                "target": canvas_id
            }]
        }]
    }

    manifest["items"].append(canvas)

    print(f"Generated: {filename} -> page{i:03d}")


# Manifestを書き出す
with open(
    f"manifests/{BOOK}.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        manifest,
        f,
        ensure_ascii=False,
        indent=2
    )

print("Manifest generated.")