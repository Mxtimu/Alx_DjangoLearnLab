# Blog CRUD Documentation

## Features
This system allows authenticated users to manage blog posts.

## Views (Class-Based)
1. **PostListView (/posts/)**: Displays all posts ordered by date.
2. **PostDetailView (/post/<pk>/)**: Shows full content of a post.
3. **PostCreateView (/post/new/)**:
   - Requires Login.
   - Automatically assigns the current user as Author.
4. **PostUpdateView (/post/<pk>/update/)**:
   - Requires Login + Authorship (UserPassesTestMixin).
5. **PostDeleteView (/post/<pk>/delete/)**:
   - Requires Login + Authorship.

## Security
* **LoginRequiredMixin**: Prevents anonymous users from creating posts.
* **UserPassesTestMixin**: Prevents users from editing/deleting posts they don't own.
