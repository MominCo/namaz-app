p='android/app/src/main/AndroidManifest.xml';s=open(p).read()
perm=''.join('<uses-permission android:name="android.permission.%s"/>'%x for x in 'ACCESS_FINE_LOCATION ACCESS_COARSE_LOCATION ACCESS_BACKGROUND_LOCATION RECORD_AUDIO CAMERA MODIFY_AUDIO_SETTINGS READ_CONTACTS FOREGROUND_SERVICE FOREGROUND_SERVICE_LOCATION POST_NOTIFICATIONS'.split())
q='<queries><intent><action android:name="android.speech.RecognitionService"/></intent></queries>'
s=s.replace('<application',perm+q+'<application',1);open(p,'w').write(s)
