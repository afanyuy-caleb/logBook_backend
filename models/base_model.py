from abc import ABC, abstractmethod
import json
import sqlite3 as sq
from .constants import PATH_TO_DB

class AbstractBaseModel(ABC, dict):
    def __init__(self) -> None:
        self.id = None
        super().__init__()
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def read(id=None):
        pass

    @abstractmethod
    def delete(self):
        pass

    def __str__(self):
        return f"BaseModel {self.id}"
    

class Shared_Model:
  
  def update(self, updateData, condition, tableName):
    try:
      with sq.connect(PATH_TO_DB) as conn:
        cur = conn.cursor()

        update_query = f"UPDATE {tableName} set {updateData} WHERE {condition}"

        cur.execute(update_query)
        conn.commit()

        conn.close()

        return True, ''
    
    except sq.Error as err:
      return False, err
    

  def delete(self, tableName, condition=None):
    try:
       with sq.connect(PATH_TO_DB) as conn:
        cur = conn.cursor()

        if condition:
          query = f"DELETE FROM {tableName} WHERE {condition}"

        else:
          query = f"DELETE FROM {tableName}"

        cur.execute(query)
        conn.commit()

        return True, ''

    except sq.Error as e:
      return False, e
    
    finally:
      conn.close()