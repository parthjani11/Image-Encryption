module AES_YP (
    input wire clk,
    input wire reset,
    output reg [127:0] encrypted128
);

    // *Memory Declaration*
    reg [7:0] memory [0:45247];  // 8-bit wide, large memory
    reg [127:0] encrypted_mem [0:2828];  // Store encrypted results

    // *Ensure Memory is Loaded Correctly*
    initial begin
        $readmemb("output.mem", memory);  // Load memory contents from file
    end

    reg [127:0] in;
    wire [127:0] key128 = 128'h000102030405060708090a0b0c0d0e0f;
    reg [31:0] addr;
    integer i, file;

    wire [127:0] aes_output;

    // AES Encryption Instance
    AES_Encrypt aes_unit (
        .in(in),
        .key(key128),
        .out(aes_output)
    );

    // *Process Input & Store Output in Loop*
    always @(posedge clk or posedge reset) begin
        if (reset) begin
            addr <= 0;
            i <= 0;
        end else begin
            for (i = 0; i < 2829; i = i + 1) begin
                addr = i * 16;  // Compute memory address

                // Load 128-bit input from memory
                in = {memory[addr+15], memory[addr+14], memory[addr+13], memory[addr+12],
                      memory[addr+11], memory[addr+10], memory[addr+9], memory[addr+8],
                      memory[addr+7], memory[addr+6], memory[addr+5], memory[addr+4],
                      memory[addr+3], memory[addr+2], memory[addr+1], memory[addr]};

                // Encrypt and store
                encrypted_mem[i] = aes_output;
                encrypted128 = encrypted_mem[i];  // Assigning to output register

                // *Debugging Statements for ModelSim*
                $display("Time: %0t | i = %0d | addr = %0d | in = %h", $time, i, addr, in);
                $display("AES Output at i=%0d: %h", i, aes_output);
                
                #1;  // Small delay for debugging visibility
            end
        end
    end

    // *Write Encrypted Data to encrypted.mem*
    initial begin
        file = $fopen("encrypted.mem", "w");
        wait(i == 2828);  // Wait until all encryption is done
        for (i = 0; i < 2829; i = i + 1) begin
            $fdisplay(file, "%h", encrypted_mem[i]);  // Write encrypted 128-bit chunks to file
        end
        $fclose(file);
        $display("Encryption Complete. File encrypted.mem generated.");
        $stop;  // Stop simulation after file writing
    end

endmodule