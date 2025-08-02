import httpx
from fastapi import HTTPException

API = "https://api.vercel.com/v13/deployments"

def trigger_vercel_deploy(*, token: str, project: str, repo: str, ref: str = "main") -> str:
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "name": project,
        "gitSource": {"type": "github", "repoId": repo, "ref": ref},
        "target": "production"
    }

    try:
        r = httpx.post(API, headers=headers, json=payload, timeout=30)
        r.raise_for_status()
    except httpx.HTTPStatusError as exc:
        # Forward Vercel’s message for easier debugging
        detail = exc.response.json().get("error", {}).get("message", str(exc))
        raise HTTPException(status_code=502, detail=f"Vercel: {detail}")

    data = r.json()
    return data.get("url", "")
