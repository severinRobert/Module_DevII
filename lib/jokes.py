from blagues_api import BlaguesAPI

key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjg0Nzc3Mjg1MTc5OTMyNjcyIiwibGltaXQiOjEwMCwia2V5IjoiSXNQZ3pYSG81cWhKZnN4NjlKOHdxUmdOZzhzTnlQMUpQbjF1UVNRSW83YWJieklHOFkiLCJjcmVhdGVkX2F0IjoiMjAyMS0xMS0yOVQwOTo1MToyMyswMDowMCIsImlhdCI6MTYzODE3OTQ4M30.E-0SthXBrOYIgYG5YK5nt17qQPGSmbJcKLTBijaC2z0'


class Jokes:

    def __init__(self) -> None:
        pass

    async def get_joke(self) -> None:
        blagues = BlaguesAPI(key)
        response = await blagues.random()
        print(response.json())


j = Jokes()