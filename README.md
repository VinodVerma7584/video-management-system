# video-management-system

## Usage
``` python
python main.py
```

## Requirements
 - `PyQt5`
 - `MongoDB` (Download link: [mongodb](https://www.mongodb.com/download-center/community))
 - Details in `conf/requirements.txt`.

## Features
1. Import local videos (batch or manually).
2. Save and classify videos in local database.
3. Play videos.

## Modules
 - `./main.py`: Controller; program entry.
 - `core/main_window.py`: View; main window.
 - `core/manual_import_waindow.py`: View; manual import window.
 - `core/model.py`: Model; database operations.
 - `core/video_player_window.py`: View; video player window.

## License
 - MIT License.
