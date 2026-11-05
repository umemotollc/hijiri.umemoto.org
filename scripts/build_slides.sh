#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if ! command -v marp >/dev/null 2>&1; then
  echo "Error: marp not found. Install with: npm install -g @marp-team/marp-cli" >&2
  exit 1
fi

input_file="$root_dir/_slides_src/2026-03-01-wikimedia25.md"
output_file="$root_dir/slides/2026-03-01-wikimedia25.html"

marp --html --output "$output_file" "$input_file"

echo "Generated: $output_file"

input_file="$root_dir/_slides_src/2026-11-05-dentsudai.md"
output_file="$root_dir/slides/2026-11-05-dentsudai.html"

marp --html --output "$output_file" "$input_file"

echo "Generated: $output_file"
