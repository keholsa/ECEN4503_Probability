module regfile (input logic         clk, 
		input logic 	    we3, 
		input logic [4:0]   ra1, ra2, wa3, 
		input logic [31:0]  wd3, 
		output logic [31:0] rd1, rd2);
   
   logic [31:0] 		    rf[31:0];
   
   // three ported register file
   // read two ports combinationally

   assign ra1 <= register[rf0];
   assign ra2 <= register[rf1];
   assign wa3 <= register[rf2];
   assign wd3 <= register[rf3];
   assign we3 <= register[rf4];
   // write third port on rising edge of clock

   always_ff @ (posedge clk) 
    begin
   if(we3)
     wd3 = 1'b1;
     wa3 = 1'b1;

     wa3 <= register[wd3];

    end

   
   
   // register 0 hardwired to 0
   
   
endmodule // regfile
