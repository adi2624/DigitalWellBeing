<html>
<head>
<title>Uploading an image with a Javascript preview.</title>
<SCRIPT LANGUAGE="JavaScript">
<!-- Begin

  function DoPreview()
  {
    var filename = document.form1.filesent.value;
    var Img = new Image();
    if (navigator.appName == "Netscape")
    {
      alert("Previews do not work in Netscape.");
    }
    else
    {
      Img.src = filename;
      document.images[0].src = Img.src;
    }
  }

  function CheckUpload()
  {
    var filename = document.form1.filesent.value;
    var extension;
    var valid = true
    var Img1 = new Image()
    if (navigator.appName == "Netscape")
    {
      alert("This upload function cannot be used with Netscape.");
      valid = false;
    }
    else if (filename == '')
    {
      valid = false;
      alert("Please include a file.");
    }
    else
    {  
      extension = filename.substring(filename.length - 3, filename.length);
      if (extension.toUpperCase() != 'JPG')
      {
        valid = false;
        alert("The file must be a JPG.");
      }
      else
      {
        Img1.src = filename;
        if ((Img1.height == 0) || (Img1.width == 0))
        {
          valid = false;
          alert("The file is invalid.");
        }
        else
        {
          document.form1.height.value = Img1.height;
          document.form1.width.value = Img1.width;
        }
      }
    }
    return valid
  }
// End -->
</script>
</head>

<body>
<h3>File Upload</h3>
<p>This allows a file to be uploaded and saved in the same directory as this page.<br>
<p>After selecting the file the &quot;Preview&quot; button will display it where the 
image marker is. The height and width of the image are read using Javascript and included in the 
form as hidden variables. Further verification rejects files which do not have a 
&quot;.jpg&quot; extension.</p>
<p>The Javascript in this form is not supported by Netscape browsers.</p> 
<form method=post action="filesave.cfm" enctype=multipart/form-data name=form1 
onSubmit="return CheckUpload()">
<input type=hidden name=height value=0>
<input type=hidden name=width value=0>
<input type=file name=filesent><input type=button value="Preview" 
name="Preview" onClick="DoPreview()"><br>
<input type="submit" value="Send File">
</form>
<img name="image1">
</body>
</html>
