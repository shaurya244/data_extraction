# data_extraction

A Python-based tool to extract, parse and load data from text sources for reaction/reagent information.  
Developed by **shaurya244**.

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Repository Structure](#repository‐structure)  
- [Installation](#installation)  
- [Usage](#usage)  
  - [Quick Start](#quick-start)  
  - [Command Line / Script Usage](#command-line-script-usage)  
- [Configuration / Input Files](#configuration‐input‐files)  
- [Output / Database Insertion](#output‐database‐insertion)  
- [Examples](#examples)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)

## Overview

This project provides scripts for extracting text (e.g., reaction data or reagent lists), parsing them into structured form, and inserting them into a database. It is particularly useful when you have **raw text files** or logs and want to automate the workflow of extraction → parsing → loading.

The primary scripts include:
- `dataextract.py` – orchestrates the extraction process  
- `extract_text.py` – extracts text from source files (e.g., papers or logs)  
- `parse_reactions.py` – parses reaction information from extracted text  
- `insert_to_db.py` – loads parsed results into a database (or other storage)  
- `main.py` – main entry point tying everything together  

## Features

- Automated extraction of text from logs / raw data files  
- Parsing of reagents, reaction information, etc.  
- Loading parsed data into a structured storage (e.g., CSV, DB)  
- Modular design so each step (extract, parse, load) is separate  
- Minimal dependencies (pure Python)  

## Repository Structure

