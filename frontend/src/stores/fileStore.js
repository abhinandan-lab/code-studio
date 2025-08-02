import { defineStore } from "pinia";
import axios from "axios";

export const useFileStore = defineStore("files", {
  state: () => ({
    files: [],
    activePath: "",
    code: "",
    apiBase: "http://127.0.0.1:8000", // FastAPI URL
  }),

  actions: {
    async fetchFiles() {
      try {
        const { data } = await axios.get(`${this.apiBase}/api/files`);
        console.log("files response", data); // <- inspect structure
        this.files = data.files;
      } catch (err) {
        console.error("fetchFiles failed", err);
        throw err; // lets Vue surface the problem
      }
    },

    async loadFile(path) {
      const { data } = await axios.get(`${this.apiBase}/api/read`, {
        params: { path },
      });
      this.activePath = path;
      this.code = data.code;
    },
    async saveCode() {
      await axios.post(`${this.apiBase}/api/save`, {
        path: this.activePath,
        code: this.code,
      });
    },

    async deploy() {
      try {
        const token =
          localStorage.getItem("vercelToken") || prompt("Vercel token");
        const project =
          localStorage.getItem("vercelProject") ||
          prompt("Vercel project name");
        const repo =
          localStorage.getItem("vercelRepo") || prompt("Git repo (user/repo)");

        // cache for next time
        localStorage.setItem("vercelToken", token);
        localStorage.setItem("vercelProject", project);
        localStorage.setItem("vercelRepo", repo);

        const branch = prompt("Git branch to deploy", "main") || "main";

        const { data } = await axios.post(`${this.apiBase}/api/deploy`, {
          vercel_token: token,
          project_name: project,
          repo_url: repo,
          branch: branch,
        });

        alert(`Deployment triggered!\n\nWatch: https://${data.deployment_url}`);
      } catch (err) {
        alert(`Deploy failed: ${err.response?.data?.detail || err.message}`);
      }
    },

    // async deploy() {
    //   const token = prompt("Vercel token");
    //   const project = prompt("Vercel project name");
    //   const repo = prompt("Repo URL");
    //   const { data } = await axios.post(`${this.apiBase}/api/deploy`, {
    //     vercel_token: token,
    //     project_name: project,
    //     repo_url: repo,
    //   });
    //   alert(`Triggered: ${data.deployment_url}`);
    // },

    // async deploy() {
    //   const token =
    //     localStorage.getItem("vercelToken") || prompt("Vercel token");
    //   const project =
    //     localStorage.getItem("vercelProject") || prompt("Vercel project name");
    //   const repo = localStorage.getItem("vercelRepo") || prompt("Repo URL");

    //   localStorage.setItem("vercelToken", token);
    //   localStorage.setItem("vercelProject", project);
    //   localStorage.setItem("vercelRepo", repo);

    //   const { data } = await axios.post(`${this.apiBase}/api/deploy`, {
    //     vercel_token: token,
    //     project_name: project,
    //     repo_url: repo,
    //   });
    //   alert(`Deployment triggered: https://${data.deployment_url}`);
    // },
  },
});
