import os
import subprocess

def run_cmd(cmd_array,cmd_name,url,parent_dir,file_name_prefix):
    print(f"Running {cmd_name} on {url}")
    this_dir = f"{parent_dir}/{cmd_name}"
    try:
        os.mkdir(this_dir)
    except:
        pass
    
    try:
        result = subprocess.run(
            cmd_array,
            capture_output=True,
            text=True,
            check=True
        )

        print(f"Writting {this_dir}/{file_name_prefix}_{cmd_name}.out")
        with open(f"{this_dir}/{file_name_prefix}_{cmd_name}.out", "w") as f:
            f.write(result.stdout)

        if result.returncode != 0:
            with open(f"{this_dir}/{file_name_prefix}_{cmd_name}_error.out", "w") as f:
                f.write(result.stderr)
        
    except subprocess.CalledProcessError as e:
        return f"Scan failed: {e.stderr}"
    except subprocess.TimeoutExpired:
        return "Scan timed out"