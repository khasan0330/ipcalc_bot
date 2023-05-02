# ipcalc_bot
# How to use this image

## start a bot instance

```
docker run --name ip_calc -e BOT_TOKEN=your_bot_token  -d khdev/ipcalc
```
* **-e BOT_TOKEN** is the parameter that, token your bot (from BotFather).
* * **-d** is the parameter that runs the Docker Container in the detached mode, i.e., in the background. If you accidentally close or terminate the Command Prompt, the Docker Container will still run in the background.