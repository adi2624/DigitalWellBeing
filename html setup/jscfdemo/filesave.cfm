<html>
<head>
<title>Saving file</title>
</head>

<body>

<p>Height: <cfoutput>#form["height"]#</cfoutput><br>
<p>Width : <cfoutput>#form["width"]#</cfoutput></p>
<cfset currentdir=ExpandPath("./")>
<cfset currentdir=Left(cgi.path_translated, Len(cgi.path_translated) - 12)>
<cfset filename=CreateUUID()>
<cfset filename=CurrentDir & filename & ".jpg">
<cffile action="upload" filefield="filesent" destination=#filename# >
<p>The file has been stored</p>
<p><a href=fileupload.cfm>Upload</a> another file.</p>

</body>
</html>
