{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p style=\"text-align:center\">\n",
    "    <a href=\"https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork865-2022-01-01\" target=\"_blank\">\n",
    "    <img src=\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png\" width=\"200\" alt=\"Skills Network Logo\"  />\n",
    "    </a>\n",
    "</p>\n",
    "\n",
    "<h1 align=center><font size = 5>Assignment: SQL Notebook for Peer Assignment</font></h1>\n",
    "\n",
    "Estimated time needed: **60** minutes.\n",
    "\n",
    "## Introduction\n",
    "Using this Python notebook you will:\n",
    "\n",
    "1.  Understand the Spacex DataSet\n",
    "2.  Load the dataset  into the corresponding table in a Db2 database\n",
    "3.  Execute SQL queries to answer assignment questions \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Overview of the DataSet\n",
    "\n",
    "SpaceX has gained worldwide attention for a series of historic milestones. \n",
    "\n",
    "It is the only private company ever to return a spacecraft from low-earth orbit, which it first accomplished in December 2010.\n",
    "SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars wheras other providers cost upward of 165 million dollars each, much of the savings is because Space X can reuse the first stage. \n",
    "\n",
    "\n",
    "Therefore if we can determine if the first stage will land, we can determine the cost of a launch. \n",
    "\n",
    "This information can be used if an alternate company wants to bid against SpaceX for a rocket launch.\n",
    "\n",
    "This dataset includes a record for each payload carried during a SpaceX mission into outer space.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Download the datasets\n",
    "\n",
    "This assignment requires you to load the spacex dataset.\n",
    "\n",
    "In many cases the dataset to be analyzed is available as a .CSV (comma separated values) file, perhaps on the internet. Click on the link below to download and save the dataset (.CSV file):\n",
    "\n",
    " <a href=\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/data/Spacex.csv\" target=\"_blank\">Spacex DataSet</a>\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting sqlalchemy==1.3.9\n",
      "  Downloading SQLAlchemy-1.3.9.tar.gz (6.0 MB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.0/6.0 MB\u001b[0m \u001b[31m69.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m:00:01\u001b[0m0:01\u001b[0m\n",
      "\u001b[?25h  Preparing metadata (setup.py) ... \u001b[?25ldone\n",
      "\u001b[?25hBuilding wheels for collected packages: sqlalchemy\n",
      "  Building wheel for sqlalchemy (setup.py) ... \u001b[?25ldone\n",
      "\u001b[?25h  Created wheel for sqlalchemy: filename=SQLAlchemy-1.3.9-cp37-cp37m-linux_x86_64.whl size=1159122 sha256=c1f743bfdb06fe3cfce386fa0a3abe44edf3162ff477dd8ea24221686230d8c5\n",
      "  Stored in directory: /home/jupyterlab/.cache/pip/wheels/ef/95/ac/c232f83b415900c26553c64266e1a2b2863bc63e7a5d606c7e\n",
      "Successfully built sqlalchemy\n",
      "Installing collected packages: sqlalchemy\n",
      "  Attempting uninstall: sqlalchemy\n",
      "    Found existing installation: SQLAlchemy 1.3.24\n",
      "    Uninstalling SQLAlchemy-1.3.24:\n",
      "      Successfully uninstalled SQLAlchemy-1.3.24\n",
      "Successfully installed sqlalchemy-1.3.9\n"
     ]
    }
   ],
   "source": [
    "!pip install sqlalchemy==1.3.9\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Connect to the database\n",
    "\n",
    "Let us first load the SQL extension and establish a connection with the database\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "%load_ext sql"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv, sqlite3\n",
    "\n",
    "con = sqlite3.connect(\"my_data1.db\")\n",
    "cur = con.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "!pip install -q pandas==1.1.5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Connected: @my_data1.db'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%sql sqlite:///my_data1.db"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/jupyterlab/conda/envs/python/lib/python3.7/site-packages/pandas/core/generic.py:2882: UserWarning: The spaces in these column names will not be changed. In pandas versions < 0.14, spaces were converted to underscores.\n",
      "  both result in 0.1234 being formatted as 0.12.\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "df = pd.read_csv(\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/data/Spacex.csv\")\n",
    "df.to_sql(\"SPACEXTBL\", con, if_exists='replace', index=False,method=\"multi\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Tasks\n",
    "\n",
    "Now write and execute SQL queries to solve the assignment tasks.\n",
    "\n",
    "**Note: If the column names are in mixed case enclose it in double quotes\n",
    "   For Example \"Landing_Outcome\"**\n",
    "\n",
    "### Task 1\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "##### Display the names of the unique launch sites  in the space mission\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * sqlite:///my_data1.db\n",
      "Done.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<table>\n",
       "    <thead>\n",
       "        <tr>\n",
       "            <th>Date</th>\n",
       "            <th>Time (UTC)</th>\n",
       "            <th>Booster_Version</th>\n",
       "            <th>Launch_Site</th>\n",
       "            <th>Payload</th>\n",
       "            <th>PAYLOAD_MASS__KG_</th>\n",
       "            <th>Orbit</th>\n",
       "            <th>Customer</th>\n",
       "            <th>Mission_Outcome</th>\n",
       "            <th>Landing _Outcome</th>\n",
       "        </tr>\n",
       "    </thead>\n",
       "    <tbody>\n",
       "        <tr>\n",
       "            <td>04-06-2010</td>\n",
       "            <td>18:45:00</td>\n",
       "            <td>F9 v1.0  B0003</td>\n",
       "            <td>CCAFS LC-40</td>\n",
       "            <td>Dragon Spacecraft Qualification Unit</td>\n",
       "            <td>0</td>\n",
       "            <td>LEO</td>\n",
       "            <td>SpaceX</td>\n",
       "            <td>Success</td>\n",
       "            <td>Failure (parachute)</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>08-12-2010</td>\n",
       "            <td>15:43:00</td>\n",
       "            <td>F9 v1.0  B0004</td>\n",
       "            <td>CCAFS LC-40</td>\n",
       "            <td>Dragon demo flight C1, two CubeSats, barrel of Brouere cheese</td>\n",
       "            <td>0</td>\n",
       "            <td>LEO (ISS)</td>\n",
       "            <td>NASA (COTS) NRO</td>\n",
       "            <td>Success</td>\n",
       "            <td>Failure (parachute)</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>22-05-2012</td>\n",
       "            <td>07:44:00</td>\n",
       "            <td>F9 v1.0  B0005</td>\n",
       "            <td>CCAFS LC-40</td>\n",
       "            <td>Dragon demo flight C2</td>\n",
       "            <td>525</td>\n",
       "            <td>LEO (ISS)</td>\n",
       "            <td>NASA (COTS)</td>\n",
       "            <td>Success</td>\n",
       "            <td>No attempt</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>08-10-2012</td>\n",
       "            <td>00:35:00</td>\n",
       "            <td>F9 v1.0  B0006</td>\n",
       "            <td>CCAFS LC-40</td>\n",
       "            <td>SpaceX CRS-1</td>\n",
       "            <td>500</td>\n",
       "            <td>LEO (ISS)</td>\n",
       "            <td>NASA (CRS)</td>\n",
       "            <td>Success</td>\n",
       "            <td>No attempt</td>\n",
       "        </tr>\n",
       "    </tbody>\n",
       "</table>"
      ],
      "text/plain": [
       "[('04-06-2010', '18:45:00', 'F9 v1.0  B0003', 'CCAFS LC-40', 'Dragon Spacecraft Qualification Unit', 0, 'LEO', 'SpaceX', 'Success', 'Failure (parachute)'),\n",
       " ('08-12-2010', '15:43:00', 'F9 v1.0  B0004', 'CCAFS LC-40', 'Dragon demo flight C1, two CubeSats, barrel of Brouere cheese', 0, 'LEO (ISS)', 'NASA (COTS) NRO', 'Success', 'Failure (parachute)'),\n",
       " ('22-05-2012', '07:44:00', 'F9 v1.0  B0005', 'CCAFS LC-40', 'Dragon demo flight C2', 525, 'LEO (ISS)', 'NASA (COTS)', 'Success', 'No attempt'),\n",
       " ('08-10-2012', '00:35:00', 'F9 v1.0  B0006', 'CCAFS LC-40', 'SpaceX CRS-1', 500, 'LEO (ISS)', 'NASA (CRS)', 'Success', 'No attempt')]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%sql\n",
    "select * from SPACEXTBL limit 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * sqlite:///my_data1.db\n",
      "Done.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<table>\n",
       "    <thead>\n",
       "        <tr>\n",
       "            <th>Launch_Site</th>\n",
       "        </tr>\n",
       "    </thead>\n",
       "    <tbody>\n",
       "        <tr>\n",
       "            <td>CCAFS LC-40</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>VAFB SLC-4E</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>KSC LC-39A</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>CCAFS SLC-40</td>\n",
       "        </tr>\n",
       "    </tbody>\n",
       "</table>"
      ],
      "text/plain": [
       "[('CCAFS LC-40',), ('VAFB SLC-4E',), ('KSC LC-39A',), ('CCAFS SLC-40',)]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%sql select distinct(Launch_Site) from SPACEXTBL"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "### Task 2\n",
    "\n",
    "\n",
    "#####  Display 5 records where launch sites begin with the string 'CCA' \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * sqlite:///my_data1.db\n",
      "Done.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<table>\n",
       "    <thead>\n",
       "        <tr>\n",
       "            <th>Launch_Site</th>\n",
       "        </tr>\n",
       "    </thead>\n",
       "    <tbody>\n",
       "        <tr>\n",
       "            <td>CCAFS LC-40</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>CCAFS LC-40</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>CCAFS LC-40</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>CCAFS LC-40</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>CCAFS LC-40</td>\n",
       "        </tr>\n",
       "    </tbody>\n",
       "</table>"
      ],
      "text/plain": [
       "[('CCAFS LC-40',),\n",
       " ('CCAFS LC-40',),\n",
       " ('CCAFS LC-40',),\n",
       " ('CCAFS LC-40',),\n",
       " ('CCAFS LC-40',)]"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%sql \n",
    "select Launch_Site from SPACEXTBL\n",
    "where Launch_Site like 'CCA%' limit 5\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Task 3\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "##### Display the total payload mass carried by boosters launched by NASA (CRS)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * sqlite:///my_data1.db\n",
      "Done.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<table>\n",
       "    <thead>\n",
       "        <tr>\n",
       "            <th>sum(PAYLOAD_MASS__KG_)</th>\n",
       "        </tr>\n",
       "    </thead>\n",
       "    <tbody>\n",
       "        <tr>\n",
       "            <td>45596</td>\n",
       "        </tr>\n",
       "    </tbody>\n",
       "</table>"
      ],
      "text/plain": [
       "[(45596,)]"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%sql\n",
    "select sum(PAYLOAD_MASS__KG_) from SPACEXTBL\n",
    "where Customer='NASA (CRS)'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Task 4\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "##### Display average payload mass carried by booster version F9 v1.1\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * sqlite:///my_data1.db\n",
      "Done.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<table>\n",
       "    <thead>\n",
       "        <tr>\n",
       "            <th>AVG(PAYLOAD_MASS__KG_)</th>\n",
       "        </tr>\n",
       "    </thead>\n",
       "    <tbody>\n",
       "        <tr>\n",
       "            <td>2928.4</td>\n",
       "        </tr>\n",
       "    </tbody>\n",
       "</table>"
      ],
      "text/plain": [
       "[(2928.4,)]"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%sql\n",
    "select AVG(PAYLOAD_MASS__KG_) from SPACEXTBL\n",
    "where Booster_Version='F9 v1.1'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Task 5\n",
    "\n",
    "##### List the date when the first succesful landing outcome in ground pad was acheived.\n",
    "\n",
    "\n",
    "_Hint:Use min function_ \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * sqlite:///my_data1.db\n",
      "Done.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<table>\n",
       "    <thead>\n",
       "        <tr>\n",
       "            <th>Date</th>\n",
       "            <th>Day</th>\n",
       "            <th>Month</th>\n",
       "            <th>Year</th>\n",
       "            <th>Landing _Outcome</th>\n",
       "        </tr>\n",
       "    </thead>\n",
       "    <tbody>\n",
       "        <tr>\n",
       "            <td>22-12-2015</td>\n",
       "            <td>22</td>\n",
       "            <td>12</td>\n",
       "            <td>2015</td>\n",
       "            <td>Success (ground pad)</td>\n",
       "        </tr>\n",
       "    </tbody>\n",
       "</table>"
      ],
      "text/plain": [
       "[('22-12-2015', '22', '12', '2015', 'Success (ground pad)')]"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%sql\n",
    "select Date,substr(Date,1,2) As Day,substr(Date,4,2) As Month,substr(Date,7,4) As Year, \"Landing _Outcome\" from SPACEXTBL\n",
    "where \"Landing _Outcome\" like \"Success%\" \n",
    "order by Year, Month, Day limit 1\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Task 6\n",
    "\n",
    "##### List the names of the boosters which have success in drone ship and have payload mass greater than 4000 but less than 6000\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * sqlite:///my_data1.db\n",
      "Done.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<table>\n",
       "    <thead>\n",
       "        <tr>\n",
       "            <th>Payload</th>\n",
       "            <th>Booster_Version</th>\n",
       "            <th>Landing _Outcome</th>\n",
       "            <th>PAYLOAD_MASS__KG_</th>\n",
       "        </tr>\n",
       "    </thead>\n",
       "    <tbody>\n",
       "        <tr>\n",
       "            <td>JCSAT-14</td>\n",
       "            <td>F9 FT B1022</td>\n",
       "            <td>Success (drone ship)</td>\n",
       "            <td>4696</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>JCSAT-16</td>\n",
       "            <td>F9 FT B1026</td>\n",
       "            <td>Success (drone ship)</td>\n",
       "            <td>4600</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>SES-10</td>\n",
       "            <td>F9 FT  B1021.2</td>\n",
       "            <td>Success (drone ship)</td>\n",
       "            <td>5300</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>SES-11 / EchoStar 105</td>\n",
       "            <td>F9 FT  B1031.2</td>\n",
       "            <td>Success (drone ship)</td>\n",
       "            <td>5200</td>\n",
       "        </tr>\n",
       "    </tbody>\n",
       "</table>"
      ],
      "text/plain": [
       "[('JCSAT-14', 'F9 FT B1022', 'Success (drone ship)', 4696),\n",
       " ('JCSAT-16', 'F9 FT B1026', 'Success (drone ship)', 4600),\n",
       " ('SES-10', 'F9 FT  B1021.2', 'Success (drone ship)', 5300),\n",
       " ('SES-11 / EchoStar 105', 'F9 FT  B1031.2', 'Success (drone ship)', 5200)]"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%sql\n",
    "select Payload,Booster_Version,\"Landing _Outcome\",PAYLOAD_MASS__KG_ from SPACEXTBL\n",
    "where \"Landing _Outcome\"= 'Success (drone ship)' and PAYLOAD_MASS__KG_ > 4000 and PAYLOAD_MASS__KG_<6000"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Task 7\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "##### List the total number of successful and failure mission outcomes\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * sqlite:///my_data1.db\n",
      "Done.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<table>\n",
       "    <thead>\n",
       "        <tr>\n",
       "            <th>substr(Mission_Outcome,1,7)</th>\n",
       "            <th>count(Mission_Outcome)</th>\n",
       "        </tr>\n",
       "    </thead>\n",
       "    <tbody>\n",
       "        <tr>\n",
       "            <td>Failure</td>\n",
       "            <td>1</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>Success</td>\n",
       "            <td>100</td>\n",
       "        </tr>\n",
       "    </tbody>\n",
       "</table>"
      ],
      "text/plain": [
       "[('Failure', 1), ('Success', 100)]"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%sql\n",
    "select substr(Mission_Outcome,1,7),count(Mission_Outcome) from SPACEXTBL\n",
    "group by substr(Mission_Outcome,1,7)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Task 8\n",
    "\n",
    "\n",
    "\n",
    "##### List the   names of the booster_versions which have carried the maximum payload mass. Use a subquery\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * sqlite:///my_data1.db\n",
      "Done.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<table>\n",
       "    <thead>\n",
       "        <tr>\n",
       "            <th>Booster_Version</th>\n",
       "            <th>PAYLOAD_MASS__KG_</th>\n",
       "        </tr>\n",
       "    </thead>\n",
       "    <tbody>\n",
       "        <tr>\n",
       "            <td>F9 B5 B1048.4</td>\n",
       "            <td>15600</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>F9 B5 B1049.4</td>\n",
       "            <td>15600</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>F9 B5 B1051.3</td>\n",
       "            <td>15600</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>F9 B5 B1056.4</td>\n",
       "            <td>15600</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>F9 B5 B1048.5</td>\n",
       "            <td>15600</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>F9 B5 B1051.4</td>\n",
       "            <td>15600</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>F9 B5 B1049.5</td>\n",
       "            <td>15600</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>F9 B5 B1060.2 </td>\n",
       "            <td>15600</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>F9 B5 B1058.3 </td>\n",
       "            <td>15600</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>F9 B5 B1051.6</td>\n",
       "            <td>15600</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>F9 B5 B1060.3</td>\n",
       "            <td>15600</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>F9 B5 B1049.7 </td>\n",
       "            <td>15600</td>\n",
       "        </tr>\n",
       "    </tbody>\n",
       "</table>"
      ],
      "text/plain": [
       "[('F9 B5 B1048.4', 15600),\n",
       " ('F9 B5 B1049.4', 15600),\n",
       " ('F9 B5 B1051.3', 15600),\n",
       " ('F9 B5 B1056.4', 15600),\n",
       " ('F9 B5 B1048.5', 15600),\n",
       " ('F9 B5 B1051.4', 15600),\n",
       " ('F9 B5 B1049.5', 15600),\n",
       " ('F9 B5 B1060.2 ', 15600),\n",
       " ('F9 B5 B1058.3 ', 15600),\n",
       " ('F9 B5 B1051.6', 15600),\n",
       " ('F9 B5 B1060.3', 15600),\n",
       " ('F9 B5 B1049.7 ', 15600)]"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%sql\n",
    "select \"Booster_Version\" , \"PAYLOAD_MASS__KG_\"from SPACEXTBL\n",
    "where \"PAYLOAD_MASS__KG_\" in (select MAX(\"PAYLOAD_MASS__KG_\") from SPACEXTBL)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Task 9\n",
    "\n",
    "\n",
    "##### List the records which will display the month names, failure landing_outcomes in drone ship ,booster versions, launch_site for the months in year 2015.\n",
    "\n",
    "**Note: SQLLite does not support monthnames. So you need to use  substr(Date, 4, 2) as month to get the months and substr(Date,7,4)='2015' for year.**\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * sqlite:///my_data1.db\n",
      "Done.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<table>\n",
       "    <thead>\n",
       "        <tr>\n",
       "            <th>Date</th>\n",
       "            <th>month</th>\n",
       "            <th>year</th>\n",
       "            <th>Landing _Outcome</th>\n",
       "            <th>Booster_Version</th>\n",
       "            <th>Launch_Site</th>\n",
       "        </tr>\n",
       "    </thead>\n",
       "    <tbody>\n",
       "        <tr>\n",
       "            <td>10-01-2015</td>\n",
       "            <td>01</td>\n",
       "            <td>2015</td>\n",
       "            <td>Failure (drone ship)</td>\n",
       "            <td>F9 v1.1 B1012</td>\n",
       "            <td>CCAFS LC-40</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>14-04-2015</td>\n",
       "            <td>04</td>\n",
       "            <td>2015</td>\n",
       "            <td>Failure (drone ship)</td>\n",
       "            <td>F9 v1.1 B1015</td>\n",
       "            <td>CCAFS LC-40</td>\n",
       "        </tr>\n",
       "    </tbody>\n",
       "</table>"
      ],
      "text/plain": [
       "[('10-01-2015', '01', '2015', 'Failure (drone ship)', 'F9 v1.1 B1012', 'CCAFS LC-40'),\n",
       " ('14-04-2015', '04', '2015', 'Failure (drone ship)', 'F9 v1.1 B1015', 'CCAFS LC-40')]"
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%sql\n",
    "select Date, substr(Date, 4, 2) as month , substr(Date,7,4) as year, \"Landing _Outcome\",Booster_Version,Launch_Site from SPACEXTBL\n",
    "where year='2015' and \"Landing _Outcome\"='Failure (drone ship)'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Task 10\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "##### Rank the  count of  successful landing_outcomes between the date 04-06-2010 and 20-03-2017 in descending order.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * sqlite:///my_data1.db\n",
      "Done.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<table>\n",
       "    <thead>\n",
       "        <tr>\n",
       "            <th>Landing _Outcome</th>\n",
       "            <th>count(*)</th>\n",
       "        </tr>\n",
       "    </thead>\n",
       "    <tbody>\n",
       "        <tr>\n",
       "            <td>Success (drone ship)</td>\n",
       "            <td>5</td>\n",
       "        </tr>\n",
       "        <tr>\n",
       "            <td>Success (ground pad)</td>\n",
       "            <td>3</td>\n",
       "        </tr>\n",
       "    </tbody>\n",
       "</table>"
      ],
      "text/plain": [
       "[('Success (drone ship)', 5), ('Success (ground pad)', 3)]"
      ]
     },
     "execution_count": 152,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "%%sql\n",
    "SELECT \"Landing _Outcome\" ,count(*) FROM SPACEXTBL \n",
    "where CAST(substr(Date,7,4) AS INTEGER) BETWEEN 2011 and 2016\n",
    "or (CAST(substr(Date,4,2) AS INTEGER)>05 and CAST(substr(Date,7,4) AS INTEGER)=2010 ) \n",
    "or (CAST(substr(Date,4,2) AS INTEGER)=06 and CAST(substr(Date,7,4) AS INTEGER)=2010 and (CAST(substr(Date,1,2) AS INTEGER)>04))\n",
    "or (CAST(substr(Date,4,2) AS INTEGER)<03 and CAST(substr(Date,7,4) AS INTEGER)=2017 ) \n",
    "or (CAST(substr(Date,4,2) AS INTEGER)=03 and CAST(substr(Date,7,4) AS INTEGER)=2017 and (CAST(substr(Date,1,2) AS INTEGER)<20))\n",
    "Group by \"Landing _Outcome\" having \"Landing _Outcome\" like \"%Success%\"\n",
    "order by Count(*) DESC"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Reference Links\n",
    "\n",
    "* <a href =\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20String%20Patterns%20-%20Sorting%20-%20Grouping/instructional-labs.md.html?origin=www.coursera.org\">Hands-on Lab : String Patterns, Sorting and Grouping</a>  \n",
    "\n",
    "*  <a  href=\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Built-in%20functions%20/Hands-on_Lab__Built-in_Functions.md.html?origin=www.coursera.org\">Hands-on Lab: Built-in functions</a>\n",
    "\n",
    "*  <a  href=\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sub-queries%20and%20Nested%20SELECTs%20/instructional-labs.md.html?origin=www.coursera.org\">Hands-on Lab : Sub-queries and Nested SELECT Statements</a>\n",
    "\n",
    "*   <a href=\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Module%205/DB0201EN-Week3-1-3-SQLmagic.ipynb\">Hands-on Tutorial: Accessing Databases with SQL magic</a>\n",
    "\n",
    "*  <a href= \"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Module%205/DB0201EN-Week3-1-4-Analyzing.ipynb\">Hands-on Lab: Analyzing a real World Data Set</a>\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Author(s)\n",
    "\n",
    "<h4> Lakshmi Holla </h4>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Other Contributors\n",
    "\n",
    "<h4> Rav Ahuja </h4>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Change log\n",
    "| Date | Version | Changed by | Change Description |\n",
    "|------|--------|--------|---------|\n",
    "| 2021-07-09 | 0.2 |Lakshmi Holla | Changes made in magic sql|\n",
    "| 2021-05-20 | 0.1 |Lakshmi Holla | Created Initial Version |\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## <h3 align=\"center\"> © IBM Corporation 2021. All rights reserved. <h3/>\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python",
   "language": "python",
   "name": "conda-env-python-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
