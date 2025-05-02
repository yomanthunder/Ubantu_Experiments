## Cammands 
### This code will help find a custom folder and send scrrenshots into it 
### I wanted to save my images in a specifc folder unlike the default one 

- Make sure you have gnome-screenshot installed if not 
```
sudo apt install gnome-screenshot

mkdir -p ~/bin/custom_screenshot
nano ~/bin/custom_screenshot
// Now copy paste the code in it 

```

### Now Create a Custom Keyboard Shortcut:
Open Settings > Keyboard > Keyboard Shortcuts

Scroll to the bottom → Click "Custom Shortcut"

Name: Custom Screenshot

Command: /home/hp/bin/my-screenshot.sh

Set a shortcut like Shift + PrtSc or anything unused

### Future features
- filling gaps dynamically on image deletion
- 


