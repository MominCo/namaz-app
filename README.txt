Namaz & Tasks (PWA)
1. Folder ko https hosting par daalein (Netlify/GitHub Pages/Firebase Hosting) ya: python -m http.server
2. Chrome/Edge: address bar ka Install icon ya app ka ⬇ Install App button = laptop desktop/mobile home screen par app aa jata hai. iPhone: Share > Add to Home Screen.
3. Login/Cloud/Chat/Calls: firebase-config.js me Firebase config paste karein. Firebase me Authentication (Email + Google) aur Firestore on karein, Firestore rules:
rules_version='2';service cloud.firestore{match /databases/{d}/documents{
 match /data/users/{u}/{p=**}{allow read,write:if request.auth.uid==u}
 match /chat/{f}/msgs/{m}{allow read,create:if request.auth!=null}
 match /loc/{f}/m/{u}{allow read:if request.auth!=null;allow write:if request.auth.uid==u}
 match /calls/{f}{allow read,write:if request.auth!=null}
 match /calls/{f}/{c}/{x}{allow read,write:if request.auth!=null}}}
4. AI: Settings > AI key me apni Anthropic API key daalein (sirf aap ke device me save hoti hai).
5. Voice: neeche right ka 🎤 dabayein aur bolein. AI jawab bol kar bhi sunata hai.
6. FREE AI: aistudio.google.com/apikey se Gemini key banayein aur Settings me 'FREE Gemini key' me daalein.
7. Voice: 'open youtube', 'discord kholo', 'call Ali', 'location kholo' bolein.
