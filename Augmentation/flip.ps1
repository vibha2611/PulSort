#Reference: Adam Dimech's blog post https://code.adonline.id.au/rotate-or-flip-images-powershell/#:~:text=Rotation%20Options,not%20to%20flip%20the%20image.

#TODO accept user input for dir

$path = "C:\Users\vibha\Documents\PHASE SUBBAND\vflip"

[System.Reflection.Assembly]::LoadWithPartialName("System.Drawing")
Get-ChildItem -recurse ($path) -include @("*.png") |
ForEach-Object {
  $image = [System.Drawing.image]::FromFile( $_ )
  $image.rotateflip("RotateNoneFlipY") #for other options like flipping along X axis see the linked blog post
  $image.save($_)
}
