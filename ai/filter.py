#
# Copyright (c) 2017-2021 VIVO.
# All Rights Reserved.
# Confidential and Proprietary - VIVO.
#
# @author: huziliang@vivo.com
# @time: 2025/06/11 09:16:23

import json
import re
import argparse


def filter_papers_by_keywords(jsonl_file, keywords):
    """
    Filter papers from a JSONL file based on keywords with fuzzy matching.

    Args:
        jsonl_file (str): Path to the JSONL file
        keywords (list): List of keywords to search for

    Returns:
        list: List of papers containing any of the keywords
    """
    matching_papers = []

    with open(jsonl_file, "r", encoding="utf-8") as f:
        for line in f:
            paper = json.loads(line.strip())

            # Search in title and summary
            title = paper.get("title", "").lower()
            summary = paper.get("summary", "").lower()

            # Create fuzzy patterns for each keyword
            for keyword in keywords:
                # Split keyword into words
                words = keyword.lower().split()
                # Create pattern that allows for variations
                pattern = r"\b" + r"\s*".join(words) + r"\b"

                # Check if pattern matches
                if re.search(pattern, title) or re.search(pattern, summary):
                    matching_papers.append(paper)
                    break  # Found a match, no need to check other keywords

    return matching_papers


# Example usage:
keywords = [
    # Image/Video Super Resolution
    "super resolution",
    "super-resolution",
    "superresolution",
    "upscaling",
    "upsampling",
    "high resolution",
    "single image super resolution",
    "sisr",
    "reference-based sr",
    "reference super resolution",
    "refsr",
    "blind super resolution",
    "blind sr",
    "zero-shot super resolution",
    "zero-shot sr",
    "real-world super resolution",
    "real-world sr",
    "real sr",
    "arbitrary scale super resolution",
    "arbitrary scale sr",
    "continuous super resolution",
    "continuous sr",
    # Video Processing
    "video super resolution",
    "video restoration",
    "video enhancement",
    "frame interpolation",
    "temporal consistency",
    "video frame interpolation",
    "video frame prediction",
    "video prediction",
    "video generation",
    "video synthesis",
    "video-to-video translation",
    "video style transfer",
    "video stabilization",
    "video denoising",
    "video deblurring",
    "vsr",
    "temporal super resolution",
    "multi-frame super resolution",
    "mfsr",
    "dynamic super resolution",
    "dsr",
    "adaptive super resolution",
    "asr",
    "video inpainting",
    "video completion",
    "video matting",
]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, required=True, help="jsonl data file")
    return parser.parse_args()


def main():
    args = parse_args()
    matching_papers = filter_papers_by_keywords(args.data, keywords)

    # 如果matching_papers为空，则保留原始文件中的第一个paper
    if len(matching_papers) == 0:
        matching_papers = [
            json.loads(open(args.data, "r", encoding="utf-8").readlines()[0])
        ]

    # Replace newlines in comments and summaries with spaces
    for paper in matching_papers:
        if "comment" in paper and paper["comment"] is not None:
            paper["comment"] = paper["comment"].replace("\n", " ")
        if "summary" in paper and paper["summary"] is not None:
            paper["summary"] = paper["summary"].replace("\n", " ")

    # save to jsonl
    with open(
        args.data.replace(".jsonl", "_filtered.jsonl"), "w", encoding="utf-8"
    ) as f:
        for paper in matching_papers:
            f.write(json.dumps(paper) + "\n")


if __name__ == "__main__":
    main()
