# 📌 Plateforme Question-Réponse (Django)

## 📖 Description

Ce projet est une plateforme web de type **Question / Réponse** inspirée de StackOverflow.
Les utilisateurs peuvent poser des questions, répondre, voter et interagir avec la communauté.

---

## 🎯 Objectifs

* Permettre aux utilisateurs de poser des questions
* Répondre aux questions
* Voter (upvote / downvote)
* Gérer les tags
* Interface d’administration pour modération

---

## ⚙️ Technologies utilisées

* **Backend** : Python, Django
* **Base de données** : SQLite (par défaut)
* **Frontend** : HTML, CSS
* **Autres** : Django ORM, Templates

---

## 🛠️ Installation

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/Badr899/platforme-Q-A.git
cd platforme_QA
```

---

### 2️⃣ Créer un environnement virtuel

```bash
python -m venv venv
```

Activer :

* Windows :

```bash
venv\Scripts\activate
```

* Linux / Mac :

```bash
source venv/bin/activate
```

---

### 3️⃣ Installer les dépendances

```bash
pip install django
```

---

### 4️⃣ Appliquer les migrations

```bash
python manage.py migrate
```

---

### 5️⃣ Créer un super utilisateur

```bash
python manage.py createsuperuser
```

---

### 6️⃣ Lancer le serveur

```bash
python manage.py runserver
```

Accéder à l’application :

👉 http://127.0.0.1:8000/

---

## 👤 Fonctionnalités principales

### 🔹 Utilisateur

* Inscription / Connexion
* Ajouter une question
* Ajouter une réponse
* Voter (upvote / downvote)
* Voir les questions par tag

### 🔹 Admin

* Gestion des questions
* Gestion des tags
* Suppression de contenu

---

## 🗂️ Structure du projet

```
project/
│
├── question/
├── answer/
├── tag/
├── vote/
├── comments
├── users
├── static/
└── base/
└── manage.py
```

---

## 🧠 Concepts utilisés

* Relations Django (ForeignKey, ManyToMany)
* Système d’authentification
* Décorateurs (`login_required`, `staff_member_required`)
* Formulaires (forms.py)
* ORM Django

---

## 🚀 Améliorations possibles

* Ajouter pagination
* Ajouter recherche avancée
* Notifications utilisateur
* API REST avec Django REST Framework

---

## 👨‍💻 Auteur

* Badr Benhilal - Anas Erchicha - Rayan Ettahiri

---

## 📌 Remarque

Ce projet a été réalisé dans un cadre pédagogique pour apprendre Django et le développement web.
