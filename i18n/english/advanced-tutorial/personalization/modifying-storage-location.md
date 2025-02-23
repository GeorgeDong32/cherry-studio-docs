---
icon: floppy-disk
---

# Modifying Storage Location

Cherry Studio data storage follows system conventions, and data is automatically placed in the user directory. The specific directory locations are as follows:

> macOS: /Users/username/Library/Application Support/CherryStudioDev

> Windows: C:\Users\username\AppData\Roaming\CherryStudio

If you wish to modify the storage location, you can do so by creating a symbolic link (symlink). Exit the application, move the data to your desired location, and then create a link in the original location pointing to the moved location.

<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

For detailed steps, please refer to: [https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880](https://github.com/CherryHQ/cherry-studio/issues/621#issuecomment-2588652880)
