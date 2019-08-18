# enemstats-backend
Server for the ENEM data api


# Samples
https://enemstats-api.herokuapp.com/api/schools/:id

or 

https://enemstats-api.herokuapp.com/api/schools?q=<query>&year=<year>&state=<state>

#Enemstats API

#Endpoints
**Search school**
----
  <_Additional information about your API call. Try to use verbs that match both request type (fetching vs modifying) and plurality (one vs multiple)._>
  Fetch multiple schools by name and year

* **URL**

  <_The URL Structure (path only, no root url)_>
  /schools
  
* **Method:**
  
  `GET` 
  
*  **URL Params**

   **Required:**
 
   `q=[string]`
   `year=[int]`
   
   **Optional:**
 
   `state=[string]`
   
* **Success Response:**
  
  * **Code:** 200 <br />
    **Content:** 
    `{
        "number_of_results": 1,
        "results": [
            {
            "avg_ch": "568.88908",
            "avg_cn": "583.34253",
            "avg_essay": "672.29885",
            "avg_lc": "581.05517",
            "avg_math": "656.20517",
            "city": "NATAL",
            "id": "5ce6eae87e06c8d09d014d16",
            "name": "COLEGIO SALESIANO SAO JOSE",
            "region": "Nordeste",
            "state": "Rio Grande do Norte",
            "type": "PRIVADA",
            "year": "2011"
            }
        ]
    }`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ results: [] }`

* **Sample Call:**
  `curl https://enemstats-api.herokuapp.com/api/schools?q=salesiano%20sao%20jose&year=2011`
