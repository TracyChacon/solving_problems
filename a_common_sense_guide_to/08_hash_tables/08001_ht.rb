# variables

#  Scope Level,Prefix,Visibility
#  Global,$,Visible everywhere in the entire program.
#  Constant,A-Z,Visible everywhere (but warns if changed).
#  Class Variable,@@,"Visible to the Class and all its ""children"" (instances)."
#  Instance Variable,@,Visible to all methods within a specific object.
#  Local Variable,a-z,Only visible within the immediate block/method/file.


# hashes, hash functions

$menu = {
    "french fries" => 0.75,
    "hamburger" => 2.5,
    "hot dog" => 1.5,
    "soda" => 0.6
}


p $menu
puts $menu


# classes 

class Restaurant
    attr_reader :menu
    attr_accessor :name

    def initialize(name)
        @name = name
        @menu = { "french fries" => 0.75,"hamburger" => 2.5,"hot dog" => 1.5,"soda" => 0.6 }
    end


    def update_price(item, new_price)
        if @menu.key?(item) && new_price > 0
            @menu[item] = new_price
            puts "Success: #{item} is now $#{new_price}"
        else
            puts "Error: Invalid items or price"
        end
    end

    # def print_menu
    #     p @menu
    # end

    # def add_item(name, price)
    #     @menu[name] = price
    # end
end

## testing class

# my_cafe = Restaurant.new


# place = Restaurant.new("food spot")

# 1. Someone tries to break the menu (Fails)
# place.menu = { "free_food" => 0.0 } 
# Result: NoMethodError

# 2. You update a price correctly (Succeeds)
# place.update_price("hamburger", 3.0)
# Result: "Success: hamburger is now $3.0"

# 3. You try an invalid update (Caught by your logic)
# place.update_price("hamburger", -5.0)
# Result: "Error: Invalid item or price!"



# hash table, hash function 

thesaurus = {}

## Array Subset

$arr_a = ["a", "b", "c", "d", "e", "f"]
$arr_b = ["b", "d", "f"]
$arr_c = ["b", "d", "f", "h"]


