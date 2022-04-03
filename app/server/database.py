import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.players

player_collection = database.get_collection("players_collection")

# add helper functions
def player_helper(player) -> dict:
    return {
        "id": str(player["_id"]),
        "first_name": player["first_name"],
        "last_name": player["last_name"],
        "weight": player["weight"],
        "age": player["age"],
        "position": player["position"],
        "height": player["height"],
        "country": player["country"],
        "club": player["club"],
    }

# retrieve all player present in the database
async def retrieve_players():
    players = []
    async for player in player_collection.find():
        players.append(player_helper(player))
    return players

# add a new player to the database
async def add_player(player_data: dict) -> dict:
    player = await player_collection.insert_one(player_data)
    new_player = await player_collection.find_one({"_id": player.inserted_id})
    return player_helper(new_player)

# fetch a player that matches an id in the record
async def retrieve_player(id: str) -> dict:
    player = await player_collection.find_one({"_id": ObjectId(id)})
    if player:
        return player_helper(player)

# update a player info with a matching id
async def update_player(id: str, data: dict):
    # return false if empty
    if len(data) < 1:
        return false
    player = await player_collection.find_one({"_id": ObjectId(id)})
    if player:
        updated_player = await player_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_player:
            return True
        return False

# delete a player from database
async def delete_player(id: str):
    player = await player_collection.find_one({"_id": ObjectId(id)}) 
    if player:
        await player_collection.delete_one({"_id": ObjectId(id)})
        return True
