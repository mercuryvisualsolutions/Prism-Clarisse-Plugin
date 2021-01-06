SETX CLARISSE_STARTUP_SCRIPT %USERPROFILE%/AppData/Roaming/Isotropix/Clarisse/4.0/scripts/PrismInit.py
SETX CLARISSE_PRISM_DIR %USERPROFILE%/Documents/clarisse/4.0/prism

robocopy \\assets\Sources\3D\Prism\Prism_Clarisse_Plugin\config  /e  %userprofile%\AppData\Roaming\Isotropix\Clarisse\4.0
robocopy \\assets\Sources\3D\Prism\Prism_Clarisse_Plugin\scripts  /e  %userprofile%\AppData\Roaming\Isotropix\Clarisse\\4.0\scripts
robocopy \\assets\Sources\3D\Prism\Prism_Clarisse_Plugin\icons  /e  %userprofile%\Documents\clarisse\4.0\prism\icons
robocopy \\assets\Sources\3D\Prism\Prism_Clarisse_Plugin\plugin  /e  %userprofile%\Documents\clarisse\4.0\prism
robocopy \\assets\Sources\3D\Prism\Prism_Clarisse_Plugin\prism  /e  C:\Prism\Plugins\Apps
robocopy \\assets\Sources\3D\Prism\Prism_Clarisse_Plugin\fix  /e  C:\Prism\Scripts

pause