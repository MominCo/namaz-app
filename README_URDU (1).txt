NAMAZ & TASKS - SAB KUCH ASAN STEPS ME

A) FIREBASE (5 minute, ek baar)  console.firebase.google.com -> project my-life-1470e
 1. Build > Authentication > Get started > Email/Password ON, Google ON.
 2. Build > Firestore Database > Create database (production mode).
 3. Firestore > Rules tab > firestore.rules file ka text paste karke Publish.
 4. Authentication > Settings > Authorized domains > apni github.io website add karein (step B ke baad).

B) FREE WEBSITE (server) - GitHub
 1. github.com par account banayein > New repository (naam: namaz-app, Public).
 2. "uploading an existing file" se is zip ke andar ki SAB files/folders (web, .github, scripts, package.json ...) upload karein.
 3. Repo > Settings > Pages > Source = "GitHub Actions". Actions tab me "Deploy web" chalne dein.
 4. Aap ki website: https://AAPKA-NAAM.github.io/namaz-app/  (ye link family ko bhejein, Chrome me Install App dabayein)

C) ASLI ANDROID APP (APK)
 1. Repo > Actions tab > "Build APK" > Run workflow. 5-10 minute lagte hain.
 2. Complete hone par us run me neeche "Artifacts" se namaz-tasks-apk download karein, zip khol kar app-debug.apk phone me install karein ("Unknown source" allow karein).
 3. APK me background location, mic se voice, WhatsApp/Discord/YouTube app seedha khulna chalta hai.
 NOTE: APK me Google sign-in nahi chalta, Email sign-in use karein.

D) AI (free): aistudio.google.com/apikey se key lein, app Settings me daalein.
