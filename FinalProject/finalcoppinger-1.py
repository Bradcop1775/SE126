#W6D1 Class Lab

#Bradley Coppinger 
#Final
#9/4/2024

#Final

# Variable List

#Main Code

# WoW Addon Creator Game
# This game helps users generate Lua code for WoW addons in an RPG-style adventure.

import time

def main():
    while True:
        print("\nWelcome, Hero! You stand on the brink of forging your path as a master coder.")
        print("Your journey begins now! Choose your profession wisely, for it will determine the power of your creation.\n")

        # Profession Selection
        professions = {
            "1": "Guildmaster (Manages guild-related events)",
            "2": "Archivist (Tracks achievements and records)",
            "3": "Spy (Monitors PvP events)",
            "4": "Enchanter (Customizes UI elements)",
            "5": "Exit Game"
        }

        for key, value in professions.items():
            print(f"{key}. {value}")

        profession_choice = input("\nChoose your profession: ")

        if profession_choice == "1":
            guildmaster_path()
        elif profession_choice == "2":
            archivist_path()
        elif profession_choice == "3":
            spy_path()
        elif profession_choice == "4":
            enchanter_path()
        elif profession_choice == "5":
            print("\nFarewell, Hero! May your addons bring glory to Azeroth!")
            break
        else:
            print("\nInvalid choice. Please choose a valid profession.")

def guildmaster_path():
    while True:
        print("\nYour profession as Guildmaster is chosen!")
        print("Set out on your quest to create your guild's first mighty script.")
        print("How should your guild respond to new heroes joining its ranks?\n")

        print("1. Welcome with a custom message")
        print("2. Announce their arrival to all guild members")
        print("3. Prepare a custom celebration with sound")
        print("4. Return to Main Menu")

        feature_choice = input("\nChoose how to welcome guild members: ")

        if feature_choice == "1":
            welcome_message = input("\nEnter the message you want to greet new arrivals with: ")
            generate_guild_welcome_code(welcome_message)
            if not play_again():
                break
        elif feature_choice == "2":
            announcement_message = input("\nEnter the announcement message for new guild members: ")
            generate_guild_announcement_code(announcement_message)
            if not play_again():
                break
        elif feature_choice == "3":
            celebration_message = input("\nEnter the celebration message: ")
            sound_file = input("Enter the path to the sound file (e.g., 'Sound\\Interface\\LevelUp.wav'): ")
            generate_guild_celebration_code(celebration_message, sound_file)
            if not play_again():
                break
        elif feature_choice == "4":
            break
        else:
            print("\nInvalid choice. Please choose a valid option.")

def archivist_path():
    while True:
        print("\nAs an Archivist, you aim to record the feats of heroes.")
        print("What achievements would you like to track?\n")

        print("1. Track when a player earns any achievement")
        print("2. Track specific achievements by ID")
        print("3. Log achievements to a file")
        print("4. Return to Main Menu")

        feature_choice = input("\nChoose your tracking method: ")

        if feature_choice == "1":
            generate_achievement_tracker_code()
            if not play_again():
                break
        elif feature_choice == "2":
            achievement_ids = input("\nEnter the achievement IDs to track (separated by commas): ")
            generate_specific_achievement_tracker_code(achievement_ids)
            if not play_again():
                break
        elif feature_choice == "3":
            generate_achievement_logger_code()
            if not play_again():
                break
        elif feature_choice == "4":
            break
        else:
            print("\nInvalid choice. Please choose a valid option.")

def spy_path():
    while True:
        print("\nAs a Spy, you keep an eye on enemy activities.")
        print("What PvP events would you like to monitor?\n")

        print("1. Alert when entering a battleground")
        print("2. Track honorable kills")
        print("3. Monitor duels")
        print("4. Return to Main Menu")

        feature_choice = input("\nChoose the PvP event to monitor: ")

        if feature_choice == "1":
            generate_battleground_alert_code()
            if not play_again():
                break
        elif feature_choice == "2":
            generate_honorable_kills_tracker_code()
            if not play_again():
                break
        elif feature_choice == "3":
            generate_duel_monitor_code()
            if not play_again():
                break
        elif feature_choice == "4":
            break
        else:
            print("\nInvalid choice. Please choose a valid option.")

def enchanter_path():
    while True:
        print("\nAs an Enchanter, you weave magic into the UI.")
        print("What UI customization would you like to create?\n")

        print("1. Add a custom minimap button")
        print("2. Create a custom frame with a message")
        print("3. Change the appearance of action bars")
        print("4. Return to Main Menu")

        feature_choice = input("\nChoose your enchantment: ")

        if feature_choice == "1":
            tooltip_text = input("\nEnter the tooltip text for the minimap button: ")
            generate_minimap_button_code(tooltip_text)
            if not play_again():
                break
        elif feature_choice == "2":
            frame_message = input("\nEnter the message to display on the custom frame: ")
            generate_custom_frame_code(frame_message)
            if not play_again():
                break
        elif feature_choice == "3":
            generate_action_bar_customization_code()
            if not play_again():
                break
        elif feature_choice == "4":
            break
        else:
            print("\nInvalid choice. Please choose a valid option.")

def play_again():
    while True:
        print("\nWhat would you like to do next?")
        print("1. Return to Main Menu")
        print("2. Exit Game")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            return True
        elif choice == "2":
            print("\nFarewell, Hero! May your addons bring glory to Azeroth!")
            exit()
        else:
            print("\nInvalid choice. Please choose a valid option.")

# Guildmaster Code Generators
def generate_guild_welcome_code(message):
    lua_code = f'''
-- Guild Welcome Addon
-- Sends a custom welcome message to new guild members when they come online.

-- Create a frame to listen for guild roster updates
local frame = CreateFrame("FRAME")

-- Register the event that triggers when the guild roster is updated
-- This event fires when guild members log in or out
frame:RegisterEvent("GUILD_ROSTER_UPDATE")

-- Event handler function
frame:SetScript("OnEvent", function(self, event, ...)
    -- Get the number of guild members
    local numGuildMembers = GetNumGuildMembers()

    -- Loop through each guild member
    for i = 1, numGuildMembers do
        -- Retrieve guild member information
        local name, _, _, _, _, _, _, _, _, _, _, _, isOnline = GetGuildRosterInfo(i)

        -- Check if the guild member is online
        if isOnline then
            -- Send a welcome message in guild chat
            SendChatMessage("{message} " .. name .. "!", "GUILD")
        end
    end
end)
'''
    save_lua_code(lua_code)

def generate_guild_announcement_code(message):
    lua_code = f'''
-- Guild Announcement Addon
-- Announces new guild members to all existing guild members.

-- Create a frame to listen for guild roster updates
local frame = CreateFrame("FRAME")

-- Register the event that triggers when the guild roster is updated
frame:RegisterEvent("GUILD_ROSTER_UPDATE")

-- Table to keep track of known guild members
local knownGuildMembers = {{}}

-- Event handler function
frame:SetScript("OnEvent", function(self, event, ...)
    -- Get the number of guild members
    local numGuildMembers = GetNumGuildMembers()

    -- Loop through each guild member
    for i = 1, numGuildMembers do
        -- Retrieve guild member information
        local name = GetGuildRosterInfo(i)

        -- Check if this is a new guild member
        if not knownGuildMembers[name] then
            -- Announce the new member to the guild
            SendChatMessage("{message} " .. name .. " has joined the guild!", "GUILD")
            -- Add the new member to the known list
            knownGuildMembers[name] = true
        end
    end
end)
'''
    save_lua_code(lua_code)

def generate_guild_celebration_code(message, sound_file):
    lua_code = f'''
-- Guild Celebration Addon
-- Celebrates new guild members with a custom message and sound.

-- Create a frame to listen for guild roster updates
local frame = CreateFrame("FRAME")

-- Register the event that triggers when the guild roster is updated
frame:RegisterEvent("GUILD_ROSTER_UPDATE")

-- Table to keep track of known guild members
local knownGuildMembers = {{}}

-- Event handler function
frame:SetScript("OnEvent", function(self, event, ...)
    -- Get the number of guild members
    local numGuildMembers = GetNumGuildMembers()

    -- Loop through each guild member
    for i = 1, numGuildMembers do
        -- Retrieve guild member information
        local name = GetGuildRosterInfo(i)

        -- Check if this is a new guild member
        if not knownGuildMembers[name] then
            -- Play the celebration sound
            PlaySoundFile("{sound_file}", "Master")
            -- Send the celebration message to guild chat
            SendChatMessage("{message} " .. name .. " has joined us! Let's celebrate!", "GUILD")
            -- Add the new member to the known list
            knownGuildMembers[name] = true
        end
    end
end)
'''
    save_lua_code(lua_code)

# Archivist Code Generators
def generate_achievement_tracker_code():
    lua_code = '''
-- Achievement Tracker Addon
-- Tracks when any player earns an achievement and announces it in guild chat.

-- Create a frame to listen for achievement events
local frame = CreateFrame("FRAME")

-- Register the event that triggers when an achievement is earned
frame:RegisterEvent("ACHIEVEMENT_EARNED")

-- Event handler function
frame:SetScript("OnEvent", function(self, event, ...)
    -- Get the ID of the achievement earned
    local achievementID = ...

    -- Get achievement information
    local achievementLink = GetAchievementLink(achievementID)

    -- Announce the achievement in guild chat
    SendChatMessage("Congratulations! Achievement earned: " .. achievementLink, "GUILD")
end)
'''
    save_lua_code(lua_code)

def generate_specific_achievement_tracker_code(achievement_ids):
    ids = [id.strip() for id in achievement_ids.split(",")]
    ids_table = "{" + ", ".join(ids) + "}"
    lua_code = f'''
-- Specific Achievement Tracker Addon
-- Tracks when specific achievements are earned and announces them in guild chat.

-- Table of achievement IDs to track
local trackedAchievements = {ids_table}

-- Create a frame to listen for achievement events
local frame = CreateFrame("FRAME")

-- Register the event that triggers when an achievement is earned
frame:RegisterEvent("ACHIEVEMENT_EARNED")

-- Event handler function
frame:SetScript("OnEvent", function(self, event, ...)
    -- Get the ID of the achievement earned
    local achievementID = ...

    -- Check if the achievement is one we're tracking
    for _, id in ipairs(trackedAchievements) do
        if id == achievementID then
            -- Get achievement information
            local achievementLink = GetAchievementLink(achievementID)

            -- Announce the achievement in guild chat
            SendChatMessage("Well done! Tracked achievement earned: " .. achievementLink, "GUILD")
            break
        end
    end
end)
'''
    save_lua_code(lua_code)

def generate_achievement_logger_code():
    lua_code = '''
-- Achievement Logger Addon
-- Logs achievements to a SavedVariables file for later review.

-- Create a frame to listen for achievement events
local frame = CreateFrame("FRAME")

-- Register the event that triggers when an achievement is earned
frame:RegisterEvent("ACHIEVEMENT_EARNED")

-- Initialize the saved variable table
MyAddonSavedAchievements = MyAddonSavedAchievements or {}

-- Event handler function
frame:SetScript("OnEvent", function(self, event, ...)
    -- Get the ID of the achievement earned
    local achievementID = ...

    -- Get achievement information
    local achievementLink = GetAchievementLink(achievementID)
    local timestamp = date("%Y-%m-%d %H:%M:%S")

    -- Log the achievement in the saved variables
    table.insert(MyAddonSavedAchievements, {id = achievementID, name = achievementLink, time = timestamp})

    -- Notify the player
    print("Achievement logged: " .. achievementLink)
end)
'''
    save_lua_code(lua_code)

# Spy Code Generators
def generate_battleground_alert_code():
    lua_code = '''
-- Battleground Alert Addon
-- Alerts the player when they enter a battleground.

-- Create a frame to listen for zone changes
local frame = CreateFrame("FRAME")

-- Register the event that triggers when the player changes zones
frame:RegisterEvent("ZONE_CHANGED_NEW_AREA")

-- Event handler function
frame:SetScript("OnEvent", function(self, event, ...)
    -- Check if the player is in a battleground
    if UnitInBattleground("player") then
        -- Alert the player
        print("You have entered a battleground. Prepare for battle!")
        -- Optional: Play a sound
        PlaySound(SOUNDKIT.PVP_ENTER_QUEUE, "Master")
    end
end)
'''
    save_lua_code(lua_code)

def generate_honorable_kills_tracker_code():
    lua_code = '''
-- Honorable Kills Tracker Addon
-- Tracks the number of honorable kills and displays them to the player.

-- Initialize the kill count
local killCount = 0

-- Create a frame to listen for combat events
local frame = CreateFrame("FRAME")

-- Register the event that triggers when combat log updates
frame:RegisterEvent("COMBAT_LOG_EVENT_UNFILTERED")

-- Event handler function
frame:SetScript("OnEvent", function(self, event)
    -- Retrieve combat event information
    local _, subEvent, _, sourceGUID = CombatLogGetCurrentEventInfo()

    -- Check if the event is an honorable kill made by the player
    if subEvent == "PARTY_KILL" and sourceGUID == UnitGUID("player") then
        -- Increment the kill count
        killCount = killCount + 1
        -- Display the updated kill count to the player
        print("Honorable Kill! Total Honorable Kills: " .. killCount)
    end
end)
'''
    save_lua_code(lua_code)

def generate_duel_monitor_code():
    lua_code = '''
-- Duel Monitor Addon
-- Monitors and announces duel requests and outcomes.

-- Create a frame to listen for duel events
local frame = CreateFrame("FRAME")

-- Register events for duel requests and duel finishes
frame:RegisterEvent("DUEL_REQUESTED")
frame:RegisterEvent("DUEL_FINISHED")

-- Event handler function
frame:SetScript("OnEvent", function(self, event, ...)
    if event == "DUEL_REQUESTED" then
        -- Get the name of the challenger
        local challengerName = ...
        -- Notify the player of the duel request
        print(challengerName .. " has challenged you to a duel!")
    elseif event == "DUEL_FINISHED" then
        -- Notify the player that the duel has ended
        print("The duel has ended. Well fought!")
    end
end)
'''
    save_lua_code(lua_code)

# Enchanter Code Generators
def generate_minimap_button_code(tooltip_text):
    lua_code = f'''
-- Custom Minimap Button Addon
-- Adds a custom button to the minimap with a tooltip.

-- Create a frame for the minimap button
local button = CreateFrame("Button", "MyMinimapButton", Minimap)
button:SetSize(32, 32)
button:SetFrameStrata("MEDIUM")
button:SetFrameLevel(8)

-- Set the button's appearance using default textures
button:SetNormalTexture("Interface\\\\Buttons\\\\UI-Quickslot2")
button:SetPushedTexture("Interface\\\\Buttons\\\\UI-Quickslot-Depress")
button:SetHighlightTexture("Interface\\\\Buttons\\\\ButtonHilight-Square", "ADD")

-- Position the button on the minimap
button:SetPoint("TOPLEFT", Minimap, "TOPLEFT")

-- Add tooltip functionality
button:SetScript("OnEnter", function(self)
    -- Show the tooltip when the mouse hovers over the button
    GameTooltip:SetOwner(self, "ANCHOR_LEFT")
    GameTooltip:AddLine("{tooltip_text}")
    GameTooltip:Show()
end)
button:SetScript("OnLeave", function(self)
    -- Hide the tooltip when the mouse leaves the button
    GameTooltip:Hide()
end)

-- Add click functionality
button:SetScript("OnClick", function(self, button)
    if button == "LeftButton" then
        -- Perform an action when the button is clicked
        print("Minimap button clicked!")
    end
end)
'''
    save_lua_code(lua_code)

def generate_custom_frame_code(message):
    lua_code = f'''
-- Custom Frame Addon
-- Creates a custom frame in the UI that displays a message.

-- Create the frame and set its parent to the UIParent
local frame = CreateFrame("Frame", "MyCustomFrame", UIParent)
frame:SetSize(300, 100)  -- Set the width and height of the frame
frame:SetPoint("CENTER") -- Position the frame at the center of the screen

-- Set the frame's background color
frame.texture = frame:CreateTexture()
frame.texture:SetAllPoints()
frame.texture:SetColorTexture(0, 0, 0, 0.5) -- Semi-transparent black background

-- Add a close button to the frame
local closeButton = CreateFrame("Button", nil, frame, "UIPanelCloseButton")
closeButton:SetPoint("TOPRIGHT", frame, "TOPRIGHT")

-- Add the message text to the frame
local text = frame:CreateFontString(nil, "ARTWORK", "GameFontHighlightLarge")
text:SetPoint("CENTER")
text:SetText("{message}")

-- Show the frame when the addon is loaded
frame:Show()
'''
    save_lua_code(lua_code)

def generate_action_bar_customization_code():
    lua_code = '''
-- Action Bar Customization Addon
-- Changes the appearance of the action bar buttons.

-- Loop through action buttons 1 to 12
for i = 1, 12 do
    -- Get the action button
    local button = _G["ActionButton" .. i]
    if button then
        -- Get the icon texture of the button
        local icon = _G["ActionButton" .. i .. "Icon"]
        if icon then
            -- Set a custom texture for the action button icon
            icon:SetTexture("Interface\\\\Icons\\\\INV_Misc_QuestionMark")
        end
    end
end
'''
    save_lua_code(lua_code)

# Utility function to save Lua code with a unique filename
def save_lua_code(lua_code):
    print("\nYour trials are complete! Witness the code forged from your journey.\n")
    timestamp = time.strftime("%Y%m%d%H%M%S")
    file_name = f"addon_output_{timestamp}.lua"
    with open(file_name, "w") as file:
        file.write(lua_code)
    print(f"Victory is yours, Hero! Your addon has been forged and saved to {file_name}.")
    print("Go forth and install your creation into World of Warcraft!")

if __name__ == "__main__":
    main()
