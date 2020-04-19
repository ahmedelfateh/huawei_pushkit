## Huawei Push-kit For Huawei Android/HarmonyOS Phones

## Table of Contents

 * [Introduction](#introduction)
 * [Installation](#installation)
 * [Configuration ](#configuration )
 * [Supported Environments](#supported-environments)
 * [License](#license)
 
## Introduction

	This 

	Python sample code encapsulates APIs of the HUAWEI Push Kit server. 

	The following table describes packages of Python sample code.

	-------------------------------------------------------------------------------------
	Package          |    Description.
	----------       |    ------------------------------------------------------------------
	huawei_pushkit   |    Package where APIs of the HUAWEI Push Kit server are encapsulated.
	-------------------------------------------------------------------------------------
	
## Installation

    pip install huawei-pushkit

## Supported Environments
	Currently support Python 2.7 / 3.0.



## Configuration 
	The following table describes parameters of the initialize_app method.

	--------------------------------------------------------------------------------------------
	Parameter      |    Description
	-------------  |   ------------------------------------------------------------------------- 
	appid          |    App ID, which is obtained from app information.
	-------------  |   -------------------------------------------------------------------------
	appsecret      |    Secret access key of an app, which is obtained from app information.
	-------------  |   -------------------------------------------------------------------------
	token_server   |    URL for the Huawei OAuth 2.0 service to obtain a token, 
	please refer to Generating an App-Level Access Token.
	-------------  |   --------------------------------------------------------------------------
	push_open_url  |    URL for accessing HUAWEI Push Kit, please refer to Sending Messages.
	---------------------------------------------------------------------------------------------

## License

	pushkit Python sample is licensed under the [Apache License, [version 2.0]
	(http://www.apache.org/licenses/LICENSE-2.0).