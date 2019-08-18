# Enemstats API
API for the ENEM (Exame Nacional do Ensino Médio) standardized test data made available by the Brazilian government. 

## Endpoints

**Search schools**
----
Fetch multiple schools by name and year

* **URL**

	`/schools`

* **Method:**

	`GET`

* **URL Params**

	**Required:**

		`q=[string]`
		`year=[int]`

	**Optional:**

		`state=[string]`

* **Success Response:**

	* **Code:** 200 <br />

	* **Content:**

		```
		{
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
		}
		```

* **Error Response:**
	* **Code:** 404 NOT FOUND <br />

	* **Content:**  `{ results: [] }`

* **Sample Call:**

	`curl https://enemstats-api.herokuapp.com/api/schools?q=salesiano%20sao%20jose&year=2011`

**Show school**
----
Fetch a single school by its id

* **URL**

	`/schools/:id`

* **Method:**

	`GET`

* **Success Response:**

	* **Code:** 200 <br />

	* **Content:**
		```
		{
		  "results": [
		    {
		      "avg_ch": "568.88908",
		      "avg_cn": "583.34253",
		      "avg_essay": "672.29885",
		      "avg_lc": "581.05517",
		      "avg_mt": "656.20517",
		      "city": "NATAL",
		      "region": "Nordeste",
		      "school_name": "COLEGIO SALESIANO SAO JOSE",
		      "state": "Rio Grande do Norte",
		      "type": "PRIVADA",
		      "year": "2011"
		    }
		  ]
		}
		```
	

* **Error Response:**
	* **Code:** 404 NOT FOUND <br />

	* **Content:**  `{ results: 'ID not found' }`

* **Sample Call:**

	`curl https://enemstats-api.herokuapp.com/api/schools/5ce6eae87e06c8d09d014d16`

**Search schools by year**
----
Fetch all grades from a specific school

* **URL**

	`/schools/year`

* **Method:**

	`GET`

* **URL Params**

	**Required:**

		`name=[string]`
		`state=[string]`
		`city=[int]`

* **Success Response:**

	* **Code:** 200 <br />

	* **Content:**

		```
		{
			"number_of_results": 9,
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
				},
				
				{ 
					"year": "2010"
					"etc" : "response is too long" 
				}
			]
		}
		```

* **Error Response:**
	* **Code:** 404 NOT FOUND <br />

	* **Content:**  `{"number_of_results": 0, "results": [] }`

* **Sample Call:**

	`curl https://enemstats-api.herokuapp.com/api/schools/year?name=salesiano%20sao%20jose&state=Rio%20Grande%20do%20Norte&city=natal`

**Show state grades**
----
Fetch grades by state

* **URL**

	`/states`

* **Method:**

	`GET`

* **URL Params**

	**Required:**

		`state=[string]`
		
	**Optional:**

		`year=[int]`

* **Success Response:**

	* **Code:** 200 <br />

	* **Content:**

		```
		{
		  "number_of_results": 1,
		  "results": [
		    {
		      "avg_ch": "438.88111",
		      "avg_cn": "423.85182",
		      "avg_essay": "498.08679",
		      "avg_lc": "484.76197",
		      "avg_math": "458.73714",
		      "id": "5cfea58c281e41ff80aa5fb4",
		      "state": "Roraima",
		      "year": "2011"
		    }
		  ]
		}
		```

* **Error Response:**
	* **Code:** 404 NOT FOUND <br />

	* **Content:**  `{"number_of_results": 0,"results": []}`

* **Sample Call:**

	`curl https://enemstats-api.herokuapp.com/api/states?state=Roraima&year=2011`

**Show national grades**
----
Fetch country grades

* **URL**

	`/national`

* **Method:**

	`GET`

* **URL Params**
		
	**Optional:**

		`year=[int]`

* **Success Response:**

	* **Code:** 200 <br />

	* **Content:**

		```
		{
		  "number_of_results": 1,
		  "results": [
		    {
		      "avg_ch": "549.85475",
		      "avg_cn": "472.70081",
		      "avg_essay": "530.34056",
		      "avg_lc": "496.4468",
		      "avg_math": "463.8997",
		      "id": "5cfb1676d6a6803b89e31260",
		      "year": "2015"
		    }
		  ]
		}
		```

* **Error Response:**
	* **Code:** 404 NOT FOUND <br />

	* **Content:**  `{"number_of_results": 0,"results": []}`

* **Sample Call:**

	`curl https://enemstats-api.herokuapp.com/api/national?year=2015`

