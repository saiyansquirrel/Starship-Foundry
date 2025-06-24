import random

# Base silhouette table embedded from Starship Construction Rules
SILHOUETTES = {
    1:  {'LNGTH': '2m',   'BASECOST': '1K',   'BASECARGO': '-',    'MINCREW': '1',    'MAXCREW': '1',    'PASSCAP': '0',      'MAX DAY/CON': '3 (3d)',  'HP': '1',  'EMPL': '-',  'HTT': '1',   'SST': '1'},
    2:  {'LNGTH': '3m',   'BASECOST': '5K',   'BASECARGO': '1',    'MINCREW': '1',    'MAXCREW': '2',    'PASSCAP': '0',      'MAX DAY/CON': '5 (2d)', 'HP': '2',  'EMPL': '-',  'HTT': '3',   'SST': '2'},
    3:  {'LNGTH': '6m',   'BASECOST': '10K',  'BASECARGO': '5',    'MINCREW': '1',    'MAXCREW': '3',    'PASSCAP': '0',      'MAX DAY/CON': '21 (2wk)', 'HP': '4', 'EMPL': '1', 'HTT': '6', 'SST': '4'},
    4:  {'LNGTH': '10m',  'BASECOST': '20K',  'BASECARGO': '12',   'MINCREW': '2',    'MAXCREW': '5',    'PASSCAP': '0',      'MAX DAY/CON': '75 (2wk)', 'HP': '6', 'EMPL': '2', 'HTT': '10', 'SST': '7'},
    5:  {'LNGTH': '15m',  'BASECOST': '35K',  'BASECARGO': '18',   'MINCREW': '3',    'MAXCREW': '8',    'PASSCAP': '0',      'MAX DAY/CON': '240 (1mo)', 'HP': '9', 'EMPL': '3', 'HTT': '13', 'SST': '10'},
    6:  {'LNGTH': '22m',  'BASECOST': '55K',  'BASECARGO': '30',   'MINCREW': '5',    'MAXCREW': '12',   'PASSCAP': '0',      'MAX DAY/CON': '360 (1mo)', 'HP': '12','EMPL': '4', 'HTT': '18', 'SST': '13'},
    7:  {'LNGTH': '33m',  'BASECOST': '100K', 'BASECARGO': '100',  'MINCREW': '8',    'MAXCREW': '18',   'PASSCAP': '4',      'MAX DAY/CON': '540 (1mo)', 'HP': '16','EMPL': '5', 'HTT': '26', 'SST': '19'},
    8:  {'LNGTH': '50m',  'BASECOST': '150K', 'BASECARGO': '375',  'MINCREW': '12',   'MAXCREW': '28',   'PASSCAP': '8',      'MAX DAY/CON': '840 (1mo)', 'HP': '20','EMPL': '6', 'HTT': '33', 'SST': '23'},
    9:  {'LNGTH': '66m',  'BASECOST': '500K', 'BASECARGO': '840',  'MINCREW': '16',   'MAXCREW': '40',   'PASSCAP': '16',     'MAX DAY/CON': '4K (3mo)',  'HP': '25','EMPL': '8', 'HTT': '45', 'SST': '34'},
    10: {'LNGTH': '100m', 'BASECOST': '1M',   'BASECARGO': '3000', 'MINCREW': '24',   'MAXCREW': '60',   'PASSCAP': '24',     'MAX DAY/CON': '6K (3mo)',  'HP': '30','EMPL': '10','HTT': '52', 'SST': '36'},
    11: {'LNGTH': '150m', 'BASECOST': '3M',   'BASECARGO': '9000', 'MINCREW': '36',   'MAXCREW': '90',   'PASSCAP': '400',    'MAX DAY/CON': '16K (6mo)', 'HP': '36','EMPL': '12','HTT': '64', 'SST': '43'},
    12: {'LNGTH': '250m', 'BASECOST': '8M',   'BASECARGO': '18000','MINCREW': '125',  'MAXCREW': '140',  'PASSCAP': '2000',   'MAX DAY/CON': '25K (6mo)', 'HP': '42','EMPL': '14','HTT': '75', 'SST': '51'},
    13: {'LNGTH': '500m', 'BASECOST': '50M',  'BASECARGO': '37.5K','MINCREW': '250',  'MAXCREW': '750',  'PASSCAP': '8000',   'MAX DAY/CON': '72K (1yr)', 'HP': '49','EMPL': '16','HTT': '93', 'SST': '62'},
    14: {'LNGTH': '1km',  'BASECOST': '125M', 'BASECARGO': '312K', 'MINCREW': '500',  'MAXCREW': '1500', 'PASSCAP': '120K',   'MAX DAY/CON': '108K (1yr)', 'HP': '56','EMPL': '18','HTT': '108','SST': '67'},
    15: {'LNGTH': '2km',  'BASECOST': '300M', 'BASECARGO': '500K', 'MINCREW': '750',  'MAXCREW': '5000', 'PASSCAP': '1M',     'MAX DAY/CON': 'Farming',   'HP': '64','EMPL': '21','HTT': '129','SST': '71'},
    16: {'LNGTH': '5km',  'BASECOST': '800M', 'BASECARGO': '3.75M','MINCREW': '1000', 'MAXCREW': '7500', 'PASSCAP': '12M',    'MAX DAY/CON': 'Farming',   'HP': '72','EMPL': '24','HTT': '145','SST': '97'},
    17: {'LNGTH': '10km', 'BASECOST': '2 bn', 'BASECARGO': '31.2M','MINCREW': '2.5K','MAXCREW': '15K', 'PASSCAP': '120M',    'MAX DAY/CON': 'Farming',   'HP': '81','EMPL': '26','HTT': '171','SST': '114'},
    18: {'LNGTH': '15km', 'BASECOST': '5 bn', 'BASECARGO': '60M',  'MINCREW': '5K',   'MAXCREW': '30K',  'PASSCAP': '400M',   'MAX DAY/CON': 'Farming',   'HP': '90','EMPL': '30','HTT': '186','SST': '121'},
    19: {'LNGTH': '25km', 'BASECOST': '12 bn','BASECARGO': '450M', 'MINCREW': '10K',  'MAXCREW': '100K', 'PASSCAP': '1 bn',    'MAX DAY/CON': 'Farming',   'HP': '100','EMPL': '35','HTT': '210','SST': '140'},
    20: {'LNGTH': '100km','BASECOST': '-',    'BASECARGO': '-',    'MINCREW': '-',    'MAXCREW': '-',    'PASSCAP': '-',      'MAX DAY/CON': '-',        'HP': '-', 'EMPL': '-', 'HTT': '-',  'SST': '-'},
}

ENGINE_CLASSES = {
    1: {'esl_adj': +3, 'price_mult': 0.25},
    2: {'esl_adj': +2, 'price_mult': 0.5},
    3: {'esl_adj': +1, 'price_mult': 0.75},
    4: {'esl_adj': 0,  'price_mult': 1.0},
    5: {'esl_adj': -1, 'price_mult': 1.25},
    6: {'esl_adj': -2, 'price_mult': 2.0},
    7: {'esl_adj': -3, 'price_mult': 3.0},
}

FRAMEWORKS = [
    {'name': 'Walker',       'cost_mult': 0.7, 'fuel_mult': 2, 'base_armor': lambda sl: sl/3 + 2, 'defaults': []},
    {'name': 'Rollercraft',  'cost_mult': 0.5, 'fuel_mult': 3, 'base_armor': lambda sl: sl/4,       'defaults': []},
    {'name': 'Aerocraft',    'cost_mult': 0.8, 'fuel_mult': 4, 'base_armor': lambda sl: sl/4,       'defaults': ['Aerodynamic Wings']},
    {'name': 'Repulsorcraft','cost_mult': 1.5, 'fuel_mult': 3, 'base_armor': lambda sl: sl/5 + 1,   'defaults': []},
    {'name': 'Starship',     'cost_mult': 1.2, 'fuel_mult': 5, 'base_armor': lambda sl: sl/3,       'defaults': ['Vacuum Sealed Hull']},
]

ROLES = [
    {'name': 'Basic',      'cost_mult': 1.0, 'free_modules': []},
    {'name': 'Transport',  'cost_mult': 1.1, 'free_modules': ['Passenger Berths']},
    {'name': 'Freighter',  'cost_mult': 1.1, 'free_modules': ['Expanded Cargo Hold']},
    {'name': 'Industrial', 'cost_mult': 1.15,'free_modules': ['Refinery']},
    {'name': 'Support',    'cost_mult': 1.1, 'free_modules': ['Workshop']},
    {'name': 'Assault',    'cost_mult': 1.25,'free_modules': ['Forward Battery']},
    {'name': 'Carrier',    'cost_mult': 1.5, 'free_modules': ['Hangar Bay']},
    {'name': 'Gunship',    'cost_mult': 1.15,'free_modules': ['Weapon Hardpoints']},
    {'name': 'Recon',      'cost_mult': 1.15,'free_modules': ['Long-Range Sensors']},
    {'name': 'Warship',    'cost_mult': 1.3, 'free_modules': ['Weapon Hardpoints']},
]

MANDATORY_MODULES = [
    'Tunnel Drive',
    'NavComputer',
    'Life Support',
    'Sensors',
    'Bridge',
]

EXTRA_MODULES = [
    'Shield Generator',
    'Aerodynamic Wings',
    'Weapon Hardpoints',
    'Medical Bay',
]

def parse_cost(cost_str: str) -> int:
    multipliers = {'K': 1_000, 'M': 1_000_000, ' bn': 1_000_000_000}
    if cost_str == '-' or not cost_str:
        return 0
    for key, mult in multipliers.items():
        if cost_str.endswith(key):
            return int(float(cost_str.replace(key, '')) * mult)
    return int(float(cost_str))

def generate_random_ship() -> dict:
    sl = random.randint(7, 13)  # typical starship sizes
    base = SILHOUETTES[sl]
    framework = random.choice([f for f in FRAMEWORKS if f['name'] == 'Starship'])
    role = random.choice(ROLES)
    engine_class = random.randint(1, 7)
    engine = ENGINE_CLASSES[engine_class]

    effective_sl = max(sl + engine['esl_adj'], sl // 2)
    base_cost = parse_cost(base['BASECOST'])
    cost = int(base_cost * framework['cost_mult'] * role['cost_mult'] * engine['price_mult'])

    modules = []
    modules.extend(framework['defaults'])
    modules.extend(role['free_modules'])
    modules.extend(MANDATORY_MODULES)
    modules.append(random.choice(EXTRA_MODULES))

    return {
        'Silhouette': sl,
        'Effective Silhouette': effective_sl,
        'Framework': framework['name'],
        'Role': role['name'],
        'Engine Class': engine_class,
        'Cost': cost,
        'Modules': modules,
    }

if __name__ == '__main__':
    ship = generate_random_ship()
    for k, v in ship.items():
        if isinstance(v, list):
            print(f"{k}: {', '.join(v)}")
        else:
            print(f"{k}: {v}")
