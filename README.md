<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="https://user-images.githubusercontent.com/78688623/124183973-d81fe400-dab0-11eb-85bd-945fb7c83445.jpg" width="128" height="128">
  </a>

<!-- ABOUT -->
## About

**Aries** is a custom [**Discord**](https://discord.com/) bot solution developed within [**discord.py**](https://github.com/Rapptz/discord.py), an API wrapper written in Python.

[Use this link to invite **Aries** to your Discord server.](https://discord.com/api/oauth2/authorize?client_id=858724881004232724&permissions=8&scope=bot)

### Built With
* [Python](https://www.python.org/)

<!-- TABLE OF CONTENTS -->
#### Table of Contents
* [About](#about)
  * [Built With](#built-with)
* [Setup](#setup)
* [Commands](#commands)
  * [Admin](#admin)
  * [Music](#music)
  * [MyAnimeList](#myanimelist)

## Setup
After [inviting](https://discord.com/api/oauth2/authorize?client_id=858724881004232724&permissions=8&scope=bot) **Aries**, you can setup your guild prefix with the below usage:

* `a!prefix <prefix>`

## Commands

| Command & Usage | Description |
| ------- | ----------- |
| `a!avatar <@user>` | **Aries** will send an embed with the targeted, if any, users avatar. |
| `a!ban <@user> <reason>` | **Aries** will ban the targeted user via @ mention and use, if any, the provided reason within your guild audit log. |
| `a!cuddle <@user>` | **Aries** will send an embed with a cuddle GIF and mention both you and the targeted user. |
| `a!gif <query>` | **Aries** will query GIPHY API and upload a GIF image to the channel with the requested content. |
| `a!help` | **Aries** will send an embed with a link to this README file. |
| `a!hug <@user>` | **Aries** will send an embed with a hug GIF and mention both you and the targeted user. |
| `a!invite` | **Aries** will send an embed with invitation information for others to also add **Aries** to their guilds. |
| `a!kick` | **Aries** will kick the targeted user via @ mention and use, if any, the provided reason within your guild audit log. |
| `a!kiss <@user>` | **Aries** will send an embed with a kiss GIF and mention both you and the targeted user. |
| `a!kiss cheek <@user>` | **Aries** will send an embed with a kiss cheek GIF and mention both you and the targeted user. |
| `a!kiss forehead <@user>` | **Aries** will send an embed with a kiss forehead GIF and mention both you and the targeted user. |
| `a!kiss lips <@user>` | **Aries** will send an embed with a kiss lips GIF and mention both you and the targeted user. |
| `a!lick <@user>` | **Aries** will send an embed with a lick GIF and mention both you and the targeted user. |
| `a!mute <@user> <time> <reason>` | **Aries** will mute the targeted user via @ mention for the specified time as well as use, if any, the reason provided within an embed. |
| `a!poll <poll>` | **Aries** will send an embed with: checkmark and X reactions added enabling poll functionality in channels. |
| `a!slap <@user>` | **Aries** will send an embed with a slap GIF and mention both you and the targeted user. |
| `a!profile <@user>` | **Aries** will send an embed showing information about the user and or target. |
| `a!purge <amount>` | **Aries** will delete an amount of messages from the channel history. |
| `a!vote ` | **Aries** will send an embed with a link to the Top.gg voting page. |
| `a!unban <userID>` | **Aries** will unban the targeted user via their userID and use, if any, the provided reason within your guild audit log. |
| `a!unmute <@user>` | **Aries** will unmute the targeted user via @ mention and use, if any, the reason provided within an embed. |

### Admin

| Command & Usage | Description |
| ------- | ----------- |
| `a!prefix <prefix>` | **Aries** will change the prefix used within your guild. |

### Music

| Command & Usage | Description |
| ------- | ----------- |
| `a!connect <query>` | **Aries** will connect to connect to the channel where the command author is present. |
| `a!fs` | **Aries** will skip the content currently being played. |
| `a!play <query>` | **Aries** will query YouTube and play content from the query. |
| `a!queue <query>` | **Aries** will send an embed with the current playback queue. |

### MyAnimeList

| Command & Usage | Description |
| ------- | ----------- |
| `a!anime <query>` | **Aries** will query MAL API and send an embed with the requested content. |
| `a!manga <query>` | **Aries** will query MAL API and send an embed with the requested content. |

<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/paulranshaw/Aries
[contributors-url]: https://github.com/paulranshaw/Aries/graphs/contributors
[license-shield]: https://img.shields.io/badge/license-MIT-blue.svg
[license-url]: https://choosealicense.com/licenses/mit
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/paulranshaw