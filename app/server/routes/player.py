from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_player,
    delete_player,
    retrieve_player,
    retrieve_players,
    update_player
)
from app.server.models.player import (
    ErrorResponseModel,
    ResponseModel,
    PlayerSchema,
    UpdatePlayerModel,
)

router = APIRouter()

# create handlers for creating new players in the database

@router.post("/", response_description = "Player data added into the database")
async def add_player_data(player: PlayerSchema = Body(...)):
    player = jsonable_encoder(player)
    new_player = await add_player(player)
    return ResponseModel(new_player, "player added successfully")

# create handlers to retrieve all player data
@router.get("/", response_description="Players retrieved")
async def get_players():
    players = await retrieve_players()
    if players:
        return ResponseModel(players, "Players data retrieved successfully")
    return ResponseModel(players, "Empty list returned")


# create handler for retrieving player info by id
@router.get("/{_id}", response_description="player data retrieved successfully")
async def get_player_data(id):
    player = await retrieve_player(id)
    if player:
        return ResponseModel(player, "Player data retrieved successfully")
    return ErrorResponseModel("An eror occured", 404, "Player data does not exist")


# updating a player info by id
@router.put("/{id}")
async def update_player_data(id: str, req: UpdatePlayerModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_player = await update_player(id, req)
    if updated_player:
        return ResponseModel(

            "Player with ID: {} name updated is successful".format(id),
            "Player name updated successfully",
        )
    return ErrorResponseModel(
        "An error occured",
        404,
        "There was an error updating the player data"
    )

# delete a player record that matches an id
@router.delete("/{id}", response_description="Player data deleted from the database")
async def delete_player_data(id: str):
    deleted_player = await delete_player(id) 
    if deleted_player:
        return ResponseModel(
        "Player with ID: {} removed".format(id), "Player deleted successfully"
        )
    return ErrorResponseModel(
        "An erorr occured", 404, "Player with id {0} does not exist".format(id)
    )