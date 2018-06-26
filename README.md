# Net Present Value Calculator

![Imgur](https://i.imgur.com/HeTY4KK.png)

### Description:
This calculator takes care of the tedious steps needed to compare or combine two dollar amounts at different points in time. Often, an item or event is recorded with two data points, a value and a time. The value recorded is the dollar amount paid at the time of the event, and the time recorded is relative to the start of a project. If two items or events wish to be compared and/or combined, their time's must be equal.

### Primary Functions:
* Basic arithmatic between two NPVs
  - Addition
  - Subtraction
  - Add an annuity payment to the value of a project
* Arithmatic with constants
  - Multiplication
  - Division
  - Make a NPV dollar value negative
* Comparisons between two NPVs
  - Equal to
  - Greater than
  - Less than
  - Greater than or equal to
  - Less than or equal to
* Special cases
  - Change the rate of an object
  - Add or subtract objects with different parameters
  - Add the NPV of an annuity to an object

### Inputs:

> An event or item requires the following information:
> * Dollar amount at the time of the event
> * Time relative to the start of the Project
>``` python
> NPV(time, value[$], rate[%])
> ```




### Tests:

16 tests exist for the NPV Calculator and can by confirmed by running `npv_unittest.py`

These tests confirm proper arithmetic and comparison functions while also ensuring proper parameters are passed in.
