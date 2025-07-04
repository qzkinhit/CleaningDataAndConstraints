# bNDCRepair

## Description
This is the implementation code for the bNDCRepair, an algorithm for repairing both aata errors and inaccurate constraints on numerical sequential data.

## Repository structure
- `Code/`: the implementation of bNDCRepair and CVtRepair
- `DataSample/`: the datasets used for experiments

## Datasets
 - **IDF**: Sensor data of an induced draft fan.

 - **NASDAQ**: Sensor data of an induced draft fan.

 - **SIM**: Simulated dataset.

 - **WADI**: Data originates from an actual water distribution network.

 - **Pump**: Sensor data monitoring a water pump.

## Comparative experiments
We compare bNDCRepair with other data cleaning methods. We implemented the algorithm CVtRepair ourselves in `Code/`.
For other methods in this article, we use the implementation in the open source repository. For the algorithms Speed ​​and Clean4TSDB, we use the implementation in repository [DataQualityGroup-MTSClean](https://github.com/dx0o0/DataQualityGroup-MTSClean); for the algorithm Holoclean, we use the implementation in repository [MDCBaseline](https://github.com/qzkinhit/MDCBaseline).

## Requirements
- Python 3.6 or higher version
- pandas
- numpy

## Usage

### runing
Once you have prepared your environment, it is already runnable. We have prepared an example for you, just run:
```shell
python ./Example.py
```
You can get the results of bNDCRepair running on the IDF dataset.

### Configures
You can change the mining settings in `/Example.py`. You can follow the format of function `IDF_10000_15`, provide a new dataset and corresponding constraints, and call the bNDCRepair algorithm for cleaning.