#W6D1 Class Lab

#Bradley Coppinger 
#Final
#9/4/2024

#Final

# Variable List

#Main Code

print("Welcome, Hero! You stand on the brink of forging your path as a master coder. Choose your profession wisely, for it will determine the power of your creation.")

# Choose profession (Lua Addon Type)
print("1. Guildmaster (Manages guild-related events)")
print("2. Archivist (Tracks achievements and records)")
print("3. Spy (Monitors PvP events)")

profession_choice = input("Choose your profession: ")

if profession_choice == "1":
    print("Your profession as Guildmaster is chosen!")
    print("How should your guild respond to new heroes joining its ranks?")
    print("1. Welcome with a message")
    print("2. Announce their arrival to all")
    print("3. Prepare a custom celebration")
    
    feature_choice = input("Choose how to welcome guild members: ")
    
    if feature_choice == "1":
        welcome_message = input("Enter the message you want to greet new arrivals with: ")
        
        lua_code = f'''
        -- Guildmaster Welcome Script
        local frame = CreateFrame("FRAME")
        frame:RegisterEvent("GUILD_ROSTER_UPDATE")
        
        frame:SetScript("OnEvent", function(self, event, ...)
            local numGuildMembers = GetNumGuildMembers()
            for i = 1, numGuildMembers do
                local name, _, _, _, _, _, _, _, _, _, _, _, isOnline = GetGuildRosterInfo(i)
                if isOnline then
                    SendChatMessage("{welcome_message} " .. name .. "!", "GUILD")
                end
            end
        end)
        '''
        # Save the generated Lua code to a file
        with open("addon_output.lua", "w") as file:
            file.write(lua_code)
        
        print("Victory is yours, Hero! Your addon has been forged and saved to addon_output.lua.")
