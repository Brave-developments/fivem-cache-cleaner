# Cache Cleaner

A Python script that automatically cleans various cache folders on Windows, specifically designed for FiveM server administrators and users who want to maintain optimal system performance.

## Features

- **FiveM Cache Cleaning**: Clears all FiveM-related cache folders
  - Main FiveM cache
  - Server cache (private)
  - Server cache (private cl2)
- **System Cache Cleaning**: Clears common Windows cache folders
  - User temp folder
  - Windows temp folder
  - Windows prefetch folder

## Requirements

- Windows 10/11
- Python 3.6 or higher
- Administrator privileges (for some system folders)

## Installation

1. Clone or download this repository to your desired location
2. Ensure Python is installed on your system
3. Update the Python path in `autoon.bat` if needed

## Usage

### Manual Execution

Run the script manually using one of these methods:

**Option 1: Using Python directly**
```bash
python clear_cache.py
```

**Option 2: Using the batch file**
```bash
autoon.bat
```

### Automated Weekly Execution

You can schedule this script to run automatically every week using Windows Task Scheduler. Here are the steps:

#### Method 1: Using Windows Task Scheduler (Recommended)

1. **Open Task Scheduler**
   - Press `Win + R`, type `taskschd.msc`, and press Enter
   - Or search for "Task Scheduler" in the Start menu

2. **Create Basic Task**
   - Click "Create Basic Task" in the right panel
   - Name: `Cache Cleaner Weekly`
   - Description: `Automatically cleans FiveM and system cache folders weekly`

3. **Set Trigger**
   - Select "Weekly"
   - Choose your preferred day (e.g., Sunday)
   - Set time (e.g., 2:00 AM when system is typically idle)

4. **Set Action**
   - Select "Start a program"
   - Program/script: `C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python312\python.exe`
   - Add arguments: `"D:\bot\cache cleaner\clear_cache.py"`
   - Start in: `D:\bot\cache cleaner`

5. **Configure Settings**
   - Check "Run with highest privileges" (required for system folders)
   - Select "Run whether user is logged on or not"
   - Choose "Run as soon as possible after a scheduled start is missed"

6. **Finish**
   - Review your settings and click "Finish"

#### Method 2: Using Command Line (Advanced)

Create a scheduled task using PowerShell:

```powershell
# Run as Administrator
SCHTASKS /CREATE /SC WEEKLY /D SUN /TN "Cache Cleaner Weekly" /TR "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python312\python.exe \"D:\bot\cache cleaner\clear_cache.py\"" /ST 02:00 /RU SYSTEM /RL HIGHEST /F
```

#### Method 3: Using the Batch File with Task Scheduler

1. Follow Method 1 steps but use:
   - Program/script: `cmd.exe`
   - Add arguments: `/c "D:\bot\cache cleaner\autoon.bat"`

## File Structure

```
cache cleaner/
├── clear_cache.py    # Main Python script
├── autoon.bat        # Batch file for easy execution
└── README.md         # This file
```

## What Gets Cleaned

### FiveM Cache Folders
- `%USERPROFILE%\AppData\Local\FiveM\FiveM.app\data\cache`
- `%USERPROFILE%\AppData\Local\FiveM\FiveM.app\data\server-cache-priv`
- `%USERPROFILE%\AppData\Local\FiveM\FiveM.app\data\server-cache-priv-cl2`

### System Cache Folders
- `%USERPROFILE%\AppData\Local\Temp`
- `C:\Windows\Temp` (requires admin)
- `C:\Windows\Prefetch` (requires admin)

## Safety Features

- The script only deletes files within specified cache folders
- Error handling prevents crashes if files are in use
- Detailed logging shows what was deleted
- No system files are touched

## Troubleshooting

### Common Issues

1. **Permission Denied**
   - Run the script as Administrator
   - Ensure the scheduled task has "Run with highest privileges" enabled

2. **Python Not Found**
   - Update the Python path in `autoon.bat`
   - Ensure Python is installed and in your system PATH

3. **Task Scheduler Not Working**
   - Check Windows Event Viewer for errors
   - Verify the task is enabled and not disabled
   - Test the script manually first

### Logs

The script provides console output showing:
- Which folders are being cleaned
- Files that were successfully deleted
- Any errors encountered during deletion

## Customization

You can modify `clear_cache.py` to:
- Add or remove cache folders
- Change the cleaning behavior
- Add additional logging
- Implement different cleaning strategies

## Security Note

This script requires administrator privileges to clean system folders. Always review the code before running it, and ensure you understand what folders will be cleaned.

## License

This project is open source. Feel free to modify and distribute as needed.

## Support

If you encounter issues or have questions, please check the troubleshooting section above or create an issue in the repository.
