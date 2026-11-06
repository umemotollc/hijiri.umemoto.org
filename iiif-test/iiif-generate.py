from PIL import Image
import json
import glob
import os

BASE = "https://hijiri.umemoto.org/iiif-test"

BOOK = "MATSUMURA-Sotojiro-Passport-1931"

files = sorted(
    glob.glob("sotojiro-passport/*.jpeg")
)

manifest = {
    "@context": "http://iiif.io/api/presentation/3/context.json",
    "id": f"{BASE}/manifests/{BOOK}.json",
    "type": "Manifest",
    "label": {
        "ja": ["砺波市美術館所蔵 松村外次郎 パスポート 1931年 日本"],
        "en": ["MATSUMURA Sotojiro Passport 1931, Japan"]
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

    filename = os.path.basename(filepath)

    with Image.open(filepath) as img:
        width, height = img.size

    image_id = f"{BASE}/images/{BOOK}/page{i:03d}"

    canvas_id = f"{BASE}/manifests/{BOOK}/canvas/p{i}"

    canvas = {
        "id": canvas_id,
        "type": "Canvas",
        "label": {
            "ja": [f"{i}フレーム"],
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

os.makedirs("manifests", exist_ok=True)

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
