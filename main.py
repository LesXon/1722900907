from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler

from routers.PersonsRouters import persons_router
from routers.IdsTypesRouters import idsTypes_router
from routers.IdsRouters import ids_router
from routers.PhonesRouters import phones_router
from routers.CellPhonesRouters import cellPhones_router
from routers.SocialNetworksRouters import socialNetworks_router
from routers.SocialNetworksTypesRouters import socialNetworksTypes_router
from routers.ContinentsRouters import continents_router
from routers.CountriesRouters import countries_router
from routers.StatesRouters import states_router
from routers.CitiesRouters import cities_router
from routers.DistrictsRouters import districts_router
from routers.NeighborhoodsRouters import neighborhoods_router
from routers.CitiesTypesRouters import citiesTypes_router
from routers.DistrictsTypesRouters import districtsTypes_router
from routers.ConstructionsTypesRouters import constructionsTypes_router
from routers.AddressesRouters import addresses_router
from routers.AddressesTypesRouters import addressesTypes_router
from routers.RouteNamesRouters import routeNames_router
from routers.RoutesAddressesRouters import routesAddresses_router
from routers.RoutesAddressesTypesRouters import routesAddressesTypes_router
from routers.CompaniesRouters import companies_router
from routers.EmployeesRouters import employees_router
from routers.PositionsRouters import positions_router
from routers.TypePositionsRouters import typePositions_router
from routers.SystemsRouters import systems_router
from routers.DiagramsRouters import diagrams_router
from routers.EntitiesRouters import entities_router
from routers.ProcessesRouters import processes_router
from routers.StoragesRouters import storages_router
from routers.FlowsRouters import flows_router
from routers.ProceduresManualRouters import proceduresManual_router
from routers.SystemEntitiesFormatsRouters import systemEntitiesFormats_router
from routers.SystemProcessesFormatsRouters import systemProcessesFormats_router
from routers.DataStorageFormatsRouters import dataStorageFormats_router
from routers.dataFlowformatsRouters import dataFlowformats_router
from routers.systemFormatsRouters import systemFormats_router
from routers.DataStructuresRouters import dataStructures_router
from routers.FieldDescriptionFormatsRouters import fieldDescriptionFormats_router
from routers.SystemDataStructuresformatsRouters import systemDataStructuresformats_router
from routers.DataDictionariesRouters import dataDictionaries_router
from routers.AppsRouters import apps_router
from routers.NavigationBarsRouters import navigationBars_router
from routers.AppMenusRouters import appMenus_router
from routers.LicensesRouters import licenses_router
from routers.AppTypesRouters import appTypes_router
from routers.AppMenusTypesRouters import appMenusTypes_router
from routers.NavigationBarsTypesRouters import navigationBarsTypes_router
from routers.UsersRouters import users_router
from routers.RolesRouters import roles_router
from routers.PermissionsRouters import permissions_router

app = FastAPI()
app.title = "lesxonEngine. LesXon Engine"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)

app.include_router(persons_router)
app.include_router(idsTypes_router)
app.include_router(ids_router)
app.include_router(phones_router)
app.include_router(cellPhones_router)
app.include_router(socialNetworks_router)
app.include_router(socialNetworksTypes_router)
app.include_router(continents_router)
app.include_router(countries_router)
app.include_router(states_router)
app.include_router(cities_router)
app.include_router(districts_router)
app.include_router(neighborhoods_router)
app.include_router(citiesTypes_router)
app.include_router(districtsTypes_router)
app.include_router(constructionsTypes_router)
app.include_router(addresses_router)
app.include_router(addressesTypes_router)
app.include_router(routeNames_router)
app.include_router(routesAddresses_router)
app.include_router(routesAddressesTypes_router)
app.include_router(companies_router)
app.include_router(employees_router)
app.include_router(positions_router)
app.include_router(typePositions_router)
app.include_router(systems_router)
app.include_router(diagrams_router)
app.include_router(entities_router)
app.include_router(processes_router)
app.include_router(storages_router)
app.include_router(flows_router)
app.include_router(proceduresManual_router)
app.include_router(systemEntitiesFormats_router)
app.include_router(systemProcessesFormats_router)
app.include_router(dataStorageFormats_router)
app.include_router(dataFlowformats_router)
app.include_router(systemFormats_router)
app.include_router(dataStructures_router)
app.include_router(fieldDescriptionFormats_router)
app.include_router(systemDataStructuresformats_router)
app.include_router(dataDictionaries_router)
app.include_router(apps_router)
app.include_router(navigationBars_router)
app.include_router(appMenus_router)
app.include_router(licenses_router)
app.include_router(appTypes_router)
app.include_router(appMenusTypes_router)
app.include_router(navigationBarsTypes_router)
app.include_router(users_router)
app.include_router(roles_router)
app.include_router(permissions_router)

Base.metadata.create_all(bind=engine)

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>lesxonEngine. LesXon Engine</h1>')

