import os, json
from pathlib import Path
from fastapi import HTTPException

# def list_project_files(root: str):
#     files = []
#     for dirpath, dirnames, filenames in os.walk(root):
#         rel_dir = os.path.relpath(dirpath, root)
#         for f in filenames:
#             files.append(os.path.join(rel_dir, f).replace("\\", "/"))
#     return {"files": files}

# def save_file(root: str, rel_path: str, content: str):
#     abs_path = Path(root, rel_path).resolve()
#     abs_path.parent.mkdir(parents=True, exist_ok=True)
#     with abs_path.open("w", encoding="utf-8") as fp:
#         fp.write(content)


ALLOWED_EXTS = {".js", ".ts", ".vue", ".py", ".json", ".md", ".scss", ".css"}

def list_project_files(root: str):
    files = []
    for dirpath, _, filenames in os.walk(root):
        # skip virtualenv and node_modules
        if "venv" in dirpath or "node_modules" in dirpath:
            continue
        for f in filenames:
            if Path(f).suffix in ALLOWED_EXTS:
                rel = os.path.relpath(os.path.join(dirpath, f), root)
                files.append(rel.replace("\\", "/"))
    return {"files": sorted(files)}


def save_file(root: str, rel_path: str, content: str):
    if not rel_path or rel_path.endswith(("/", "\\")):
        # Reject “empty” or directory-only paths
        raise HTTPException(status_code=400, detail="Invalid target file path")

    abs_path = Path(root, rel_path).resolve()

    # Extra safety: forbid writing outside the project root
    if root not in str(abs_path):
        raise HTTPException(status_code=400, detail="Path escapes project root")

    abs_path.parent.mkdir(parents=True, exist_ok=True)
    with abs_path.open("w", encoding="utf-8") as fp:
        fp.write(content)


def read_file(root: str, rel_path: str) -> str:
    from pathlib import Path
    abs_path = Path(root, rel_path).resolve()
    with abs_path.open("r", encoding="utf-8") as fp:
        return fp.read()

