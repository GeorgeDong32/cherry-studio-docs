---
icon: server
---

# Data Settings

On this page, you can perform cloud and local backups of client data, query the local data directory, and clear cache, among other operations.

## Data Backup

Currently, data backup only supports the WebDAV method. You can choose a service that supports WebDAV for cloud backups.

You can also achieve multi-device data synchronization by using the <mark style="color:blue;">`A`</mark>—Backup → <mark style="color:blue;">`WebDAV`</mark>—Restore → <mark style="color:blue;">`B`</mark> method.

## **Example using Nutstore**

1.  Log in to Nutstore, click on your username in the top right corner, and select “Account Info”:\


    <figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>
2.  Select “Security Options” and click “Add Application”:\


    <figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>
3.  Enter the application name and generate a random password:\


    <figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>
4.  Copy and record the password:\


    <figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>
5.  Obtain the server address, account, and password:\


    <figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>
6.  In CherryStudio Settings - Data Settings, fill in the WebDAV information:\


    <figure><img src="../../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>
7.  Select to back up or restore data, and you can set the automatic backup time cycle.\


    <figure><img src="../../../.gitbook/assets/image (47).png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
WebDAV services with lower barriers to entry are generally cloud storage services:

* [Nutstore](https://www.jianguoyun.com/)
* [123Pan](https://www.123pan.com/) (Requires membership)
* [Aliyun Drive](https://www.alipan.com/) (Requires purchase)
* [Box](https://www.box.com/) (Free storage capacity is 10GB, single file size limit is 250MB.)
* [Dropbox](https://www.dropbox.com/) (Dropbox offers 2GB for free, and you can expand to 16GB by inviting friends.)
* [TeraCloud](https://teracloud.jp/en/) (Free space is 10GB, and another 5GB of extra space can be obtained through invitations.)
* [Yandex Disk](https://disk.yandex.com/) (Free users get 10GB of storage.)

Secondly, some services require self-deployment:

* [Alist](https://alist.nn.ci/zh/)
* [Cloudreve](https://cloudreve.org/)
* [sharelist](https://github.com/reruin/sharelist)
{% endhint %}
