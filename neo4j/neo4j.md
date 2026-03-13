### Neo4j

Neo4j is a graph database management system used similar to traditional databases but with a focus on relationships between data. It uses cypher query language to interact with the database. we can create a instance locally or use the cloud based service. 

### Cypher

Cypher is a declarative query language for graph databases. It is used to create, read, update, and delete data in the database. 

### Neo4j Instance

We can create a instance locally or use the cloud based service. 

```text
- Neo4j Desktop: Neo4j Desktop is a desktop application that allows you to create and manage Neo4j instances. 

- Neo4j Aura: Neo4j Aura is a cloud based service that allows you to create and manage Neo4j instances. 

```

Following are the commands we use to manage Neo4j Database in desktop and aura mode

- ##### CREATE

```cypher
CREATE (:node_label {property_name_1: 'property_value_1', property_name_2: 'property_value_2'})

eg: 
CREATE (p:Person {name: 'John', age: 30})
CREATE (m:Movie {title: 'The Matrix', year: 1999})
CREATE (p: person {name: 'John', age: 32})
```

- ##### MATCH

```cypher
MATCH (n:node_label {property_name_1: 'property_value_1', property_name_2: 'property_value_2'})

eg: 
MATCH (p:Person {name: 'John'})
return p

```

- ##### CREATE RELATIONSHIP

```cypher
(:node1)-[:relationship]->(:node2)
(:node1)<-[:relationship]-(:node2)

Eg:
MATCH (p1:Person {name: 'John'}), (p2:Person {name: 'Jane'})
CREATE (p1)-[:KNOWS]->(p2)

(or)

MATCH (p1:Person {name: 'John'})-[:KNOWS]->(p2:Person {name: 'Jane'})
return p1, p2
```

- ##### Soting
```cypher
order by
```

- ##### CONSTRAINTS

```cypher
SHOW CONSTRAINTS  (To see the constraints)

CREATE CONSTRAINT constraint_name ON (n:node_label) ASSERT n.property_name IS UNIQUE (To create a constraint)

DROP CONSTRAINT constraint_name (To drop a constraint)
```

- ##### Updating the graph

```cypher
Keyword: set

MATCH (p:Person {name: 'John'})
SET p.age = 31
RETURN p
```


- ##### DELETE properties

```cypher
Keyword: remove

MATCH (p:Person {name: 'John'})
REMOVE p.age
RETURN p

or use set value=null
```

- ##### DELETE nodes and relationships

```cypher
Keyword: delete

MATCH (p:Person {name: 'John'})
DETACH DELETE p
RETURN p
```

##### Add a property to a relationship

```cypher
Keyword: set

MATCH (p1:Person {name: 'John'})-[k:knows]->(p2:Person {name: 'Jane'})
SET k.since = 2022
RETURN p1, p2
```

##### MERGING 

```cypher
Keyword: merge

MATCH (p1:Person {name: 'John'}), (p2:Person {name: 'Jane'})
MERGE (p1)-[:KNOWS]->(p2)
RETURN p1, p2

If the node or relationship already exists, it will not be created. If it does not exist, it will be created.
```

##### Sub Querying
We give this subquerying with in {} applying with where condition or anyother

```cypher
MATCH (person:Person)-[:WORKS_FOR]->(company)
WHERE company.name STARTS WITH "Company"
AND EXISTS {
  MATCH (person)-[:LIKES]->(t:Technology)
  WHERE COUNT { (t)<-[:LIKES]-() } >= 3
}
RETURN person.name as person, company.name AS company;
```

however we can use `UNION` keyword to combine the results of two or more queries.

```cypher
MATCH (p1:Person {name: 'John'}), (p2:Person {name: 'Jane'})
CREATE (p1)-[:KNOWS]->(p2)
UNION
MATCH (p1:Person {name: 'John'})-[:KNOWS]->(p2:Person {name: 'Jane'})
return p1, p2
```


we also have `UNWIND` keyword to expand a list into a set of rows like sql unnest

```cypher
MATCH (p:Person {name: 'John'})
UNWIND p.hobbies AS hobby
RETURN hobby
```
where it gives output as 

| hobby |
|-------|
| 'reading' |
| 'swimming' |
| 'coding' | 


`CALL` keyword is used to call a procedure or a function where it returns the result of the procedure or function. we can write our queries within this `CALL` keyword, where they will be executed initially.

```cypher
CALL {
	MATCH (p:Person)-[:LIKES]->(:Technology {type: "Java"})
	RETURN p

	UNION

	MATCH (p:Person)
	WHERE COUNT { (p)-[:IS_FRIENDS_WITH]->() } > 1
	RETURN p
}
RETURN p.name AS person, p.birthdate AS dob
ORDER BY dob DESC;
```

`OUTPUT`
| person     | dob        |
|------------|------------|
| "Joe"      | 1988-08-08 |
| "Jennifer" | 1988-01-01 |
| "John"     | 1985-04-04 |


##### FILTERS


```cypher
- exists
- where
- filter
- starts with
- ends with
- contains
- is null
- is not null
- is empty
- is not empty
```


