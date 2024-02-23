### Resume

Dalam materi ini, kita mempelajari beberapa konsep penting dalam penggunaan Git:

- **Git Versioning**: Mengatur versi dari source code program.
- **Setting Git**: Konfigurasi awal untuk memulai menggunakan Git.
- **Saving Changes**: Pengelolaan perubahan dengan menggunakan Git status, add, commit, diff, stash, dan ignore.
- **Git Log, Checkout, dan Reset**: Melihat log, beralih ke revisi tertentu, dan melakukan reset pada commit.
- **Syncing (Remote, Fetch, Push, dan Pull)**: Sinkronisasi dengan repositori remote melalui fetch, push, dan pull.
- **Branching**: Memahami konsep branch dalam Git.
- **Pull Request**: Proses mengajukan perubahan pada repositori.
- **Collaboration Considerations**: Panduan terbaik untuk struktur branch dalam kolaborasi tim.

---

#### Apa yang dimaksud dengan Versioning?

Versioning adalah proses mengatur versi dari source code program untuk memantau dan mengelola perubahan.

#### Apa itu Git?

Git adalah salah satu sistem kontrol versi yang populer di kalangan pengembang. Ini memungkinkan kolaborasi yang efisien dalam pengembangan perangkat lunak.

#### Hal yang Harus Diperhatikan Ketika Collaboration

Struktur branch yang direkomendasikan:

1. **Master**: Hanya untuk produksi.
2. **Branch Develop**: Untuk pengembangan.
3. **Branch Fitur (Contoh: Fitur A, Fitur B)**: Dibuat dari branch develop untuk pengembangan fitur tertentu.

#### Code Git yang Penting untuk Diingat

###### GIT INIT, CLONE, CONFIG

```html
<!-- git config -->
$ git config --global user.name “John Done”
$ git config --global user.email “johndoe@email.com”

<!-- start with init -->
$ git init
$ git remote add <remote_name> <remote_repo_url>$ git push -u <remote_name> <local_branch_name>

<!-- start with an existing project, start working on the project -->
$ git clone ssh://john@example.com/path/to/my-project.git
$ cd my-project
```

###### GIT DIFF AND STASH

```html
<!-- git diff -->
<!-- change file -->
<!-- add staging area -->
$ git diff --staged

<!-- stashing your work -->
$ git stash

<!-- re-applying your stashed changes -->
$ git stash apply
```

###### GIT LOG, CHECKOUT

```html
<!-- viewing an old revision -->
$ git log --oneline

<!-- b7119f2 Continue doing crazy things -->
<!-- 872fa7e Try something crazy -->
<!-- a1e8fb5 Make some important changes to hello.txt -->

$ git checkout a1e8fb5
```

###### GIT PUSH, FETCH & PULL

```html
<!-- git remote -->
$ git remote -v
$ git remote add origin http://dev.example.com/john.git

<!-- fetch and pull -->
$ git fetch
$ git pull origin master

<!-- push -->
$ git push origin master
$ git push origin feature/login-user
```

###### GIT BRANCHING

```html
<!-- show all branch -->
$ git branch --list

<!-- create a new branch called <branch> -->
$ git branch <branch>

<!-- force delete the specified branch -->
$ git branch -D <branch>

<!-- list remote branch -->
$ git branch -a
```

###### GIT MERGE

```html
<!-- Start a new feature -->
$ git checkout -b new-feature master
<!-- Edit some files -->
$ git add <file>
$ git commit -m "Start a feature"
<!-- Edit some files -->
$ git add <file>
$ git commit -m "Finish a feature"
<!-- Merge in the new-feature branch -->
$ git checkout master
$ git merge new-feature
$ git branch -d new-feature
```