# PizzaOrder Backend Documentation

## Overview
PizzaOrder is a Spring Boot REST API for managing pizza orders. The application provides endpoints for creating, reading, updating, and deleting pizza orders.

## Deployment Information
- **Environment**: Google Cloud Platform (GCP) Compute Engine
- **Access URL**: http://34.23.15.226:8080/pizza/orders
- **Port**: 8080
- **Java Version**: 17

## API Endpoints

### Base URL
```
http://34.23.15.226:8080
```

### Order Management Endpoints

#### Get All Orders
- **Method**: `GET`
- **URL**: `/pizza/orders`
- **Description**: Retrieves all pizza orders
- **Response**: Array of order strings

#### Add Order
- **Method**: `POST`
- **URL**: `/pizza/orders`
- **Content-Type**: `text/plain`
- **Request Body**: Pizza order string
- **Description**: Adds a new pizza order

#### Update Order
- **Method**: `PUT`
- **URL**: `/pizza/orders/{index}`
- **Content-Type**: `text/plain`
- **Request Body**: Updated pizza order string
- **Path Parameters**: 
  - `index`: Integer index of the order to update
- **Description**: Updates an existing pizza order at the specified index

#### Delete Order
- **Method**: `DELETE`
- **URL**: `/pizza/orders/{index}`
- **Path Parameters**: 
  - `index`: Integer index of the order to delete
- **Description**: Deletes a pizza order at the specified index


### VM ScreenShot
![VM ScreenShot](https://raw.githubusercontent.com/260427-ContactCenterGCP/suny-repo/main/Assignments/Screenshots/VM%20ScreenShot.png)

### SSH In-Browser
![SSH In-Browser](https://raw.githubusercontent.com/260427-ContactCenterGCP/suny-repo/main/Assignments/Screenshots/SSH%20In-Browser.png)

### App ScreenShot
![App Running](https://raw.githubusercontent.com/260427-ContactCenterGCP/suny-repo/main/Assignments/Screenshots/App%20Running.png)