from abc import ABC, abstractmethod
from mysql.connector import CMySQLConnection, MySQLConnection
from typing import Any

class DataManipulationLanguage:

    class DataSet(ABC):

        @abstractmethod
        def load(self) -> None:
            pass

        def rm(self, MySQL_conn: CMySQLConnection | MySQLConnection, table: str):
            self.__cursor: Any = MySQL_conn.cursor()
            self.__cursor.execute(f"DELETE FROM {table}")
            MySQL_conn.commit()
            self.__cursor.close()
    
    class Atmosphere(DataSet):

        def load(self,
                MySQL_conn: CMySQLConnection | MySQLConnection,
                rec_id: str,
                temperature: float,
                uv: float,
                pressure: float | int,
                humidity: int,
                precipitation: float,
                wind_speed: float,
                cloud: int) -> None:
            
            self.__cursor: Any = MySQL_conn.cursor()
            self.__cursor.execute("""
                                INSERT INTO atmosphere (rec_id, temperature, uv, pressure, humidity, precipitation, wind_speed, cloud)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                                  """, (rec_id, temperature, uv, pressure, humidity, precipitation, wind_speed, cloud))
            MySQL_conn.commit()
            self.__cursor.close()
        
    class State(DataSet):

        def load(self,
                MySQL_conn: CMySQLConnection | MySQLConnection,
                rec_id: int,
                is_day: int,
                will_it_rain: int,
                will_it_snow: int,
                time: str) -> None:

            self.__cursor: Any = MySQL_conn.cursor()
            self.__cursor.execute("""
                                INSERT INTO states (rec_id, is_day, will_it_rain, will_it_snow, time)
                                VALUES (%s, %s, %s, %s, %s)
                                """, (rec_id, is_day, will_it_rain, will_it_snow, time))
            MySQL_conn.commit()
            self.__cursor.close()