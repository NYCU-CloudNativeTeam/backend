from typing import Optional, Dict
from model.user_model import User
from model.base_model import db

class UserRepository:
    def find_user_by_username(self, username: str) -> Optional[User]:
        """
        Retrieve a user from the database by their username.

        This method searches the User model's database table for an entry
        that matches the provided username. If a matching user is found, 
        it returns the User object. If no user is found, it returns None.

        Args:
            username (str): The username of the user to retrieve.

        Returns:
            Optional[User]: The user object if found, otherwise None.
        """
        return User.query.filter_by(username=username).first()

    def add_user(self, user: User) -> User:
        """Add a new user to the database.

        Args:
            user (User): The user instance to be added.

        Returns:
            User: The newly added user instance.
        """
        db.session.add(user)
        db.session.commit()
        return user

    def update_user_settings(self, user: User) -> None:
        """
        Commit changes of the user object to the database.

        Args:
            user (User): The user instance with updated fields that needs to be committed.

        Returns:
            None
        """
        db.session.commit()