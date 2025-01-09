# Wuthery Localizations

The repository contains localizations for all [Wuthery](https://wuthery.com) services. If you would like to contribute, feel free to translate to any of the supported languages on your [Crowdin](https://crowdin.com/project/wuthery).

## Supported Languages

The following languages are supported by our projects:

- English (en)
- German (de)
- Spanish (es)
- French (fr)
- Indonesian (id)
- Japanese (ja)
- Korean (ko)
- Portuguese (pt)
- Russian (ru)
- Thai (th)
- Ukrainian (uk)
- Vietnamese (vi)
- Chinese (Simplified) (zh-Hans)
- Chinese (Traditional) (zh-Hant)

If you would like to see a new language added, please request it on our [Discord server](https://discord.gg/rKrbqz5utj), by [creating an issue](https://github.com/Wuthery/localizations/issues/new?title={Language}+language+request&body=Please+add+{language}+language+support+on+Wuthery.), or on [Crowdin](https://crowdin.com/project/wuthery).

## For Wuthery Developers

If you are a Wuthery developer, you should use [**localization-server**](localization-server/) to test or add new localizations during development:

1. Clone the repository:
```bash
git cone https://github.com/Wuthery/localizations.git
```
2. Install the dependencies:
```bash
uv sync
```
3. Start the server:
```bash
uv run uvicorn localization-server.app:app --reload --port 1180 --reload-include *.json
```

You then need to point your target service to the server by setting the `LOCALIZATION_SERVER_URL` in your `.env` file:
```dosini
LOCALIZATION_SERVER_URL=http://localhost:1180
```
