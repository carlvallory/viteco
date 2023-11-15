# viteco
Video Text Comparison using OBS Studio and OpenCV

## Requirements
- Python (3.7-3.10)
- [OBS Studio]
- [OBS Websocket plugin]
- Install the required packages with:
- ```pip install -r requirements.txt```

## Usage
1. Run OBS Studio and create two scenes:
    - **TV**: this is the scene that will be shown when there is no ad.
    - **ADBREAK**: this is the scene that will be shown when an ad is detected.
2. Install the OBS Websocket plugin and configure it to use the default port (4444), and enable authentication (default script password is "secret"). Restart OBS and start the websocket server.
3. Replace the words at the ```config.ini``` file with the words you want to detect to block the ads from.
4. Set the config file (```config.ini```) to your liking.
5. Run the script: ```python3 text-extractor.py```