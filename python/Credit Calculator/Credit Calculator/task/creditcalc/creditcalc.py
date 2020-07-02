import sys
from math import ceil, log, floor


def __periods(monthly, interest_month, principal):
    return ceil(
        log(
            monthly / (monthly - interest_month * principal),
            1 + interest_month)
    )


def __annuity(principal, interest_month, periods):
    return principal * __coef(interest_month, periods)


def __principal(monthly, interest_month, periods):
    return monthly / __coef(interest_month, periods)


def __coef(interest_month, periods):
    return interest_month * (interest_month + 1) ** periods / \
           ((interest_month + 1) ** periods - 1)


def __period_formatter(periods):
    years = periods // 12
    months = periods % 12

    if years == 0:
        return __month_formatter(months)
    elif months == 0:
        return __year_formatter(years)
    else:
        return f"{__year_formatter(years)} and {__month_formatter(months)}"


def __year_formatter(years):
    if years == 0:
        return ""
    elif years == 1:
        return "1 year"
    else:
        return f"{years} years"


def __month_formatter(months):
    if months == 0:
        return ""
    elif months == 1:
        return "1 month"
    else:
        return f"{months} months"


def parse_params(params):
    argument_map = {}
    for params in params:
        key_value = params.split("=")
        argument_map[key_value[0][2:]] = key_value[1]
    return argument_map


def validate_type(payment_type):
    return payment_type == "annuity" or payment_type == "diff"


def validate_payment(payment, payment_type):
    return payment_type != "diff" or payment is None


def validate_principal(principal):
    return principal is None or parse_int(principal) is not None


def validate_periods(periods):
    return periods is None or parse_int(periods) is not None


def validate_interest(interest):
    return parse_float(interest) is not None


def parse_int(num, default = None):
    try:
        return int(num)
    except ValueError:
        return default
    except TypeError:
        return default


def parse_float(num, default = None):
    try:
        return float(num)
    except ValueError:
        return default
    except TypeError:
        return default


def calculate_diff(principal, periods, interest):
    total = 0
    for period in range(1, periods + 1):
        payment = ceil(principal / periods +
                       interest *
                       (principal - (
                               principal * (period - 1)) / periods)
                       )
        total += payment
        print(f"Month {period}: paid out {payment}")
    print(f"\nOverpayment = {total - principal}")


def overpayment(periods, annuity, principal):
    return periods * annuity - principal


def calculate_annuity(payment, principal, periods, interest):
    if payment is None:
        payment = ceil(__annuity(principal, interest, periods))
        print(f"Your annuity payment = {payment}!")
        over = overpayment(periods, payment, principal)
        print(f"Overpayment = {over}")
    elif principal is None:
        principal = floor(__principal(payment, interest, periods))
        print(f"Your credit principal = {principal}!")
        over = overpayment(periods, payment, principal)
        print(f"Overpayment = {over}")
    elif periods is None:
        periods = floor(__periods(payment, interest, principal))
        print(f"You need {__period_formatter(periods)} to repay this credit!")
        over = overpayment(periods, payment, principal)
        print(f"Overpayment = {over}")


args = parse_params(sys.argv[1:])
arg_type = args["type"]
arg_payment = args.get("payment")
arg_principal = args.get("principal")
arg_periods = args.get("periods")
arg_interest = args.get("interest")

if not validate_type(arg_type) \
        or not validate_payment(arg_payment, arg_type) \
        or not validate_principal(arg_principal) \
        or not validate_periods(arg_periods) \
        or not validate_interest(arg_interest):
    print("Incorrect parameters")
    sys.exit(1)

if arg_type == "diff":
    calculate_diff(principal = parse_int(arg_principal),
                   periods = parse_int(arg_periods),
                   interest = parse_float(arg_interest) / 1200)
elif arg_type == "annuity":
    calculate_annuity(payment = parse_int(arg_payment),
                      principal = parse_int(arg_principal),
                      periods = parse_int(arg_periods),
                      interest = parse_float(arg_interest) / 1200)