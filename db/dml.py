from abc import ABC, abstractmethod
from mysql.connector import CMySQLConnection, MySQLConnection
from typing import Any

class DataManipulationLanguage:

    class DataSet(ABC):

        @abstractmethod
        def load(self) -> None:
            pass
            
        @abstractmethod
        def rm(self) -> None:
            pass
    
    class RequestForecastToken(DataSet):

        def load(self,
                MySQL_conn: CMySQLConnection | MySQLConnection,
                token: str,
                uid: int) -> None:

            self.__cursor: Any = MySQL_conn.cursor()
            self.__cursor.execute("INSERT INTO request_forecast_token (req_token, uid) VALUES (%s, %s)", (token, uid))
            MySQL_conn.commit()
            self.__cursor.close()

        def rm(self, MySQL_conn: CMySQLConnection | MySQLConnection, token: str) -> None:
            self.__cursor: Any = MySQL_conn.cursor()
            self.__cursor.execute("DELETE FROM request_forecast_token WHERE req_token = %s", (token,))
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
        
        def rm(self, MySQL_conn: CMySQLConnection | MySQLConnection, token: str) -> None:
            self.__cursor: Any = MySQL_conn.cursor()
            self.__cursor.execute("DELETE FROM atmosphere WHERE RIGHT(rec_id, 16) = %s", (token,))
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
        
        def rm(self, MySQL_conn: CMySQLConnection | MySQLConnection, token: str) -> None:
            self.__cursor: Any = MySQL_conn.cursor()
            self.__cursor.execute("DELETE FROM states WHERE RIGHT(rec_id, 16) = %s", (token,))
            MySQL_conn.commit()
            self.__cursor.close()
    
    class Opinion(DataSet):

        def load(self,
                MySQL_conn: CMySQLConnection | MySQLConnection,
                text: str,
                token: str,
                latitude: str,
                longitude: str) -> None:
            self.__cursor: Any = MySQL_conn.cursor()
            self.__cursor.execute("INSERT INTO opinions (text, token, latitude, longitude) VALUES (%s, %s, %s, %s)", (text, token, latitude, longitude))
            MySQL_conn.commit()
            self.__cursor.close()

        def rm(self, MySQL_conn: CMySQLConnection | MySQLConnection, token: str) -> None:
            self.__cursor: Any = MySQL_conn.cursor()
            self.__cursor.execute("DELETE FROM opinions WHERE token = %s", (token,))
            MySQL_conn.commit()
            self.__cursor.close()
        
        def edit(self, MySQL_conn: CMySQLConnection | MySQLConnection, token: str, new_text: str) -> None:
            self.__cursor: Any = MySQL_conn.cursor()
            self.__cursor.execute("UPDATE opinions SET text = %s WHERE token = %s", (new_text, token))
            MySQL_conn.commit()
            self.__cursor.close()
    
    class Users(DataSet):

        def load(self,
                MySQL_conn: CMySQLConnection | MySQLConnection,
                email: str,
                f_name: str,
                l_name: str,
                api_key: str) -> None:
            self.__cursor: Any = MySQL_conn.cursor()
            self.__cursor.execute("INSERT INTO users (email, first_name, last_name, api_key) VALUES (%s, %s, %s, %s)", (email, f_name, l_name, api_key))
            MySQL_conn.commit()
            self.__cursor.close()
        
        def rm(self, MySQL_conn: CMySQLConnection | MySQLConnection, uid: int) -> None:
            self.__cursor: Any = MySQL_conn.cursor()
            self.__cursor.execute("DELETE FROM users WHERE uid = %s", (uid,))
            MySQL_conn.commit()
            self.__cursor.close()