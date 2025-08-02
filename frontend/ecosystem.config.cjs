module.exports = {
  apps: [
    {
      name: "vite-dev",
      /*
       * On Windows, tell PM2 to spawn the command
       * exactly as you would type it in PowerShell/cmd.
       * Use "cmd" and the /c switch so the .cmd file is
       * handled by the shell—not by Node.
       */
      cmd: "powershell.exe",
      args: "-NoLogo -Command npm run dev",
      cwd: __dirname,
      env: { PORT: "5200" },
      autorestart: true,
      watch: false,
      max_restarts: 5
    }
  ]
};
