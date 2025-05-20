
# 🧪 TP4 – Défi : Tests d’intégration d’une API REST

---

## 🎯 Objectif du TP

Vous allez tester une **API REST simple** développée avec Flask.

Le but n’est pas uniquement de lancer des tests existants, mais de :
- Compléter les routes manquantes de l’API
- Écrire les **tests d’intégration** correspondants
- Gérer les **cas d’erreur** comme un vrai développeur back-end 🧠

---

## 🧱 Contexte

L’application expose une API avec gestion de "utilisateurs".  
Quelques routes sont déjà codées, d’autres non. À vous de compléter !

### ✅ Routes déjà disponibles :

- `POST /users` : créer un utilisateur (`{"name": "..."}` obligatoire)
- `GET /users` : récupérer tous les utilisateurs

---

## 🧩 Défis à relever

### 🔧 1. Implémenter des routes manquantes (dans `app/api.py`)

- [ ] `GET /users/<id>` : renvoie l’utilisateur avec cet ID
  - ✅ 200 si trouvé
  - ❌ 404 si non trouvé

- [ ] `DELETE /users/<id>` : supprime l’utilisateur
  - ✅ 204 si supprimé
  - ❌ 404 si ID inexistant

---

### 🧪 2. Écrire les tests d’intégration (dans `tests/test_api.py`)

- [ ] `test_get_user_by_id()` :
  - créer un utilisateur
  - le récupérer avec `/users/<id>`
  - vérifier que le nom correspond

- [ ] `test_delete_user()` :
  - créer un utilisateur
  - le supprimer
  - vérifier qu’il n’est plus accessible

- [ ] `test_delete_non_existing_user()` :
  - tenter de supprimer un ID inexistant
  - vérifier qu’on obtient un statut 404

---

### 🔎 3. Bonus (niveau +1)

- [ ] Ajouter une vérification pour les noms vides dans le `POST /users`
- [ ] Retourner une erreur 400 si `"name"` est manquant
- [ ] Ajouter un test pour ce cas

---

## 🧪 Exécution des tests

Assurez-vous que l’API est lancée dans un terminal :

```bash
python app/api.py

