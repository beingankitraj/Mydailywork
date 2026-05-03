document.addEventListener('DOMContentLoaded', () => {
    const lengthSlider = document.getElementById('length-slider');
    const lengthVal = document.getElementById('length-val');
    const generateBtn = document.getElementById('generate-btn');
    const copyBtn = document.getElementById('copy-btn');
    const passwordResult = document.getElementById('password-result');
    const toast = document.getElementById('toast');
    
    // Update length value when slider changes
    lengthSlider.addEventListener('input', () => {
        lengthVal.textContent = lengthSlider.value;
    });
    
    // Generate password
    generateBtn.addEventListener('click', async () => {
        const length = parseInt(lengthSlider.value);
        const uppercase = document.getElementById('uppercase').checked;
        const lowercase = document.getElementById('lowercase').checked;
        const numbers = document.getElementById('numbers').checked;
        const symbols = document.getElementById('symbols').checked;
        
        // Validation
        if (!uppercase && !lowercase && !numbers && !symbols) {
            showToast('Please select at least one character type!', true);
            return;
        }
        
        try {
            // Add loading state
            generateBtn.textContent = 'Generating...';
            generateBtn.disabled = true;
            
            const response = await fetch('/api/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    length,
                    uppercase,
                    lowercase,
                    numbers,
                    symbols
                })
            });
            
            const data = await response.json();
            
            if (response.ok) {
                passwordResult.value = data.password;
            } else {
                showToast(data.error || 'Failed to generate password', true);
            }
        } catch (error) {
            showToast('An error occurred. Please try again.', true);
            console.error('Error:', error);
        } finally {
            // Remove loading state
            generateBtn.textContent = 'Generate Password';
            generateBtn.disabled = false;
        }
    });
    
    // Copy to clipboard
    copyBtn.addEventListener('click', () => {
        if (!passwordResult.value) {
            return;
        }
        
        navigator.clipboard.writeText(passwordResult.value)
            .then(() => {
                showToast('Password copied to clipboard!');
            })
            .catch(err => {
                console.error('Failed to copy: ', err);
                showToast('Failed to copy password', true);
            });
    });
    
    // Show toast message
    function showToast(message, isError = false) {
        toast.textContent = message;
        
        if (isError) {
            toast.style.backgroundColor = '#ef4444'; // Red for errors
            toast.style.boxShadow = '0 10px 15px -3px rgba(239, 68, 68, 0.3)';
        } else {
            toast.style.backgroundColor = '#22c55e'; // Green for success
            toast.style.boxShadow = '0 10px 15px -3px rgba(34, 197, 94, 0.3)';
        }
        
        toast.classList.add('show');
        
        setTimeout(() => {
            toast.classList.remove('show');
        }, 3000);
    }
    
    // Generate initial password on load
    generateBtn.click();
});
